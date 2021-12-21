import falcon
import simplejson as json
import mysql.connector
import config
from datetime import datetime, timedelta, timezone
from core.useractivity import user_logger, access_control


class EmailMessageCollection:
    @staticmethod
    def __init__():
        """"Initializes EmailMessageCollection"""
        pass

    @staticmethod
    def on_options(req, resp):
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_get(req, resp):
        access_control(req)
        print(req.params)
        start_datetime_local = req.params.get('startdatetime')
        end_datetime_local = req.params.get('enddatetime')

        timezone_offset = int(config.utc_offset[1:3]) * 60 + int(config.utc_offset[4:6])
        if config.utc_offset[0] == '-':
            timezone_offset = -timezone_offset

        if start_datetime_local is None:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description="API.INVALID_START_DATETIME_FORMAT")
        else:
            start_datetime_local = str.strip(start_datetime_local)
            try:
                start_datetime_utc = datetime.strptime(start_datetime_local,
                                                       '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc) - \
                    timedelta(minutes=timezone_offset)
            except ValueError:
                raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                       description="API.INVALID_START_DATETIME_FORMAT")

        if end_datetime_local is None:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description="API.INVALID_END_DATETIME_FORMAT")
        else:
            end_datetime_local = str.strip(end_datetime_local)
            try:
                end_datetime_utc = datetime.strptime(end_datetime_local,
                                                     '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc) - \
                    timedelta(minutes=timezone_offset)
            except ValueError:
                raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                       description="API.INVALID_END_DATETIME_FORMAT")

        if start_datetime_utc >= end_datetime_utc:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   title='API.BAD_REQUEST',
                                   description='API.START_DATETIME_MUST_BE_EARLIER_THAN_END_DATETIME')

        cnx = mysql.connector.connect(**config.myems_fdd_db)
        cursor = cnx.cursor()

        query = (" SELECT id, recipient_name, recipient_email, "
                 "        subject, message, attachment_file_name, "
                 "        created_datetime_utc, scheduled_datetime_utc, status "
                 " FROM tbl_email_messages "
                 " WHERE created_datetime_utc >= %s AND created_datetime_utc < %s "
                 " ORDER BY created_datetime_utc ")
        cursor.execute(query, (start_datetime_utc, end_datetime_utc))
        rows = cursor.fetchall()

        if cursor:
            cursor.close()
        if cnx:
            cnx.disconnect()

        result = list()
        if rows is not None and len(rows) > 0:
            for row in rows:
                meta_result = {"id": row[0],
                               "recipient_name": row[1],
                               "recipient_email": row[2],
                               "subject": row[3],
                               "message": row[4].replace("<br>", ""),
                               "attachment_file_name": row[5],
                               "created_datetime": row[6].timestamp() * 1000 if isinstance(row[6], datetime) else None,
                               "scheduled_datetime":
                                   row[7].timestamp() * 1000 if isinstance(row[7], datetime) else None,
                               "status": row[8]}
                result.append(meta_result)

        resp.text = json.dumps(result)

    @staticmethod
    @user_logger
    def on_post(req, resp):
        """Handles POST requests"""
        access_control(req)

        try:
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.ERROR', description=ex)

        new_values = json.loads(raw_json)

        if 'rule_id' in new_values['data'].keys():
            if new_values['data']['rule_id'] <= 0:
                raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                       description='API.INVALID_RULE_ID')
            rule_id = new_values['data']['rule_id']
        else:
            rule_id = None

        if 'recipient_name' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['recipient_name'], str) or \
                len(str.strip(new_values['data']['recipient_name'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_RECIPIENT_NAME')
        recipient_name = str.strip(new_values['data']['recipient_name'])

        if 'recipient_email' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['recipient_email'], str) or \
                len(str.strip(new_values['data']['recipient_email'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_RECIPIENT_EMAIL')
        recipient_email = str.strip(new_values['data']['recipient_email'])

        if 'subject' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['subject'], str) or \
                len(str.strip(new_values['data']['subject'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_SUBJECT_VALUE')
        subject = str.strip(new_values['data']['subject'])

        if 'message' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['message'], str) or \
                len(str.strip(new_values['data']['message'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_MESSAGE_VALUE')
        message = str.strip(new_values['data']['message'])

        if 'attachment_file_name' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['attachment_file_name'], str) or \
                len(str.strip(new_values['data']['attachment_file_name'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_ATTACHMENT_FILE_NAME')
        attachment_file_name = str.strip(new_values['data']['attachment_file_name'])

        if 'attachment_file_object' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['attachment_file_object'], str) or \
                len(str.strip(new_values['data']['attachment_file_object'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_ATTACHMENT_FILE_OBJECT')
        attachment_file_object = str.strip(new_values['data']['attachment_file_object'])

        if 'attachment_file_object' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['attachment_file_object'], str) or \
                len(str.strip(new_values['data']['attachment_file_object'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_ATTACHMENT_FILE_OBJECT')
        attachment_file_object = str.strip(new_values['data']['attachment_file_object'])

        if 'created_datetime' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['created_datetime'], str) or \
                len(str.strip(new_values['data']['created_datetime'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_CREATED_DATETIME')
        created_datetime_local = str.strip(new_values['data']['created_datetime'])

        if 'scheduled_datetime' not in new_values['data'].keys() or \
                not isinstance(new_values['data']['scheduled_datetime'], str) or \
                len(str.strip(new_values['data']['scheduled_datetime'])) == 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_SCHEDULED_DATETIME')
        scheduled_datetime_local = str.strip(new_values['data']['scheduled_datetime'])

        timezone_offset = int(config.utc_offset[1:3]) * 60 + int(config.utc_offset[4:6])
        if config.utc_offset[0] == '-':
            timezone_offset = -timezone_offset

        if created_datetime_local is None:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description="API.INVALID_CREATED_DATETIME_FORMAT")
        else:
            created_datetime_local = str.strip(created_datetime_local)
            try:
                created_datetime_utc = datetime.strptime(created_datetime_local,
                                                         '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc) - \
                                     timedelta(minutes=timezone_offset)
            except ValueError:
                raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                       description="API.INVALID_CREATED_DATETIME_FORMAT")

        if scheduled_datetime_local is None:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description="API.INVALID_SCHEDULED_DATETIME_FORMAT")
        else:
            scheduled_datetime_local = str.strip(scheduled_datetime_local)
            try:
                scheduled_datetime_utc = datetime.strptime(scheduled_datetime_local,
                                                           '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc) - \
                                     timedelta(minutes=timezone_offset)
            except ValueError:
                raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                       description="API.INVALID_SCHEDULED_DATETIME_FORMAT")
        print(created_datetime_utc)
        print(scheduled_datetime_utc)
        status = 'new'

        cnx = mysql.connector.connect(**config.myems_fdd_db)
        cursor = cnx.cursor()
        add_row = (" INSERT INTO tbl_email_messages "
                   "             (rule_id, recipient_name, recipient_email, subject, message, "
                   "              attachment_file_name, attachment_file_object, created_datetime_utc,"
                   "              scheduled_datetime_utc, status) "
                   " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        cursor.execute(add_row, (rule_id,
                                 recipient_name,
                                 recipient_email,
                                 subject,
                                 message,
                                 attachment_file_name,
                                 attachment_file_object,
                                 created_datetime_utc,
                                 scheduled_datetime_utc,
                                 status))
        new_id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.disconnect()

        resp.status = falcon.HTTP_201
        resp.location = '/emailmessages/' + str(new_id)


class EmailMessageItem:
    @staticmethod
    def __init__():
        """"Initializes EmailMessageItem"""
        pass

    @staticmethod
    def on_options(req, resp, id_):
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_get(req, resp, id_):
        access_control(req)
        if not id_.isdigit() or int(id_) <= 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_EMAIL_MESSAGE_ID')

        cnx = mysql.connector.connect(**config.myems_fdd_db)
        cursor = cnx.cursor()

        query = (" SELECT id, recipient_name, recipient_email, "
                 "        subject, message, attachment_file_name, "
                 "        created_datetime_utc, scheduled_datetime_utc, status "
                 " FROM tbl_email_messages "
                 " WHERE id = %s ")
        cursor.execute(query, (id_,))
        row = cursor.fetchone()

        if cursor:
            cursor.close()
        if cnx:
            cnx.disconnect()

        if row is None:
            raise falcon.HTTPError(falcon.HTTP_404, title='API.NOT_FOUND',
                                   description='API.EMAIL_MESSAGE_NOT_FOUND')

        result = {"id": row[0],
                  "recipient_name": row[1],
                  "recipient_email": row[2],
                  "subject": row[3],
                  "message": row[4].replace("<br>", ""),
                  "attachment_file_name": row[5],
                  "created_datetime": row[6].timestamp() * 1000 if isinstance(row[6], datetime) else None,
                  "scheduled_datetime": row[7].timestamp() * 1000 if isinstance(row[7], datetime) else None,
                  "status": row[8]}

        resp.text = json.dumps(result)

    @staticmethod
    @user_logger
    def on_delete(req, resp, id_):
        access_control(req)
        if not id_.isdigit() or int(id_) <= 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_EMAIL_MESSAGE_ID')

        cnx = mysql.connector.connect(**config.myems_fdd_db)
        cursor = cnx.cursor()

        cursor.execute(" SELECT id "
                       " FROM tbl_email_messages "
                       " WHERE id = %s ", (id_,))
        row = cursor.fetchone()

        if row is None:
            if cursor:
                cursor.close()
            if cnx:
                cnx.disconnect()
            raise falcon.HTTPError(falcon.HTTP_404, title='API.NOT_FOUND',
                                   description='API.EMAIL_MESSAGE_NOT_FOUND')

        cursor.execute(" DELETE FROM tbl_email_messages WHERE id = %s ", (id_,))
        cnx.commit()

        if cursor:
            cursor.close()
        if cnx:
            cnx.disconnect()

        resp.status = falcon.HTTP_204
