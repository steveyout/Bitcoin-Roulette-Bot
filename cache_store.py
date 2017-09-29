from db import redisConn
import json


class UserBalanceStore(object):
    key_prefix = 'user_Balance_'

    @staticmethod
    def get_key(user_id):
        return UserBalanceStore.key_prefix + str(user_id)

    @staticmethod
    def exists(user_id):
        return redisConn.exists(UserBalanceStore.get_key(user_id))

    @staticmethod
    def get(user_id):
        try:
            return redisConn.get(UserBalanceStore.get_key(user_id)).decode('utf-8')
        except:
            return None

    @staticmethod
    def set(user_id, name):
        return redisConn.set(UserBalanceStore.get_key(user_id), name)
    
    @staticmethod
    def delete_note(user_id):
        return redisConn.delete(UserBalanceStore.get_key(user_id))

class PhotoCacheStore(object):
    key_prefix = 'photo_link_'

    @staticmethod
    def get_key(user_id):
        return PhotoCacheStore.key_prefix + str(user_id)

    @staticmethod
    def exists(user_id):
        return redisConn.exists(PhotoCacheStore.get_key(user_id))

    @staticmethod
    def get(user_id):
        try:
            return redisConn.get(PhotoCacheStore.get_key(user_id)).decode('utf-8')
        except:
            return None

    @staticmethod
    def set(user_id, name):
        return redisConn.set(PhotoCacheStore.get_key(user_id), name)
    
    @staticmethod
    def delete_note(user_id):
        return redisConn.delete(PhotoCacheStore.get_key(user_id))


class VariablesListStore(object):
    key_prefix = 'variables_list_'

    @staticmethod
    def get_key(user_id):
        return VariablesListStore.key_prefix + str(user_id)

    @staticmethod
    def get(user_id):
        list_str = redisConn.get(VariablesListStore.get_key(user_id))
        if list_str is None:
            return None
        return json.loads(list_str.decode('utf-8'))

    @staticmethod
    def set(user_id, friends_list):
        return redisConn.set(VariablesListStore.get_key(user_id), json.dumps(friends_list))

    @staticmethod
    def delete_note(user_id):
        return redisConn.delete(VariablesListStore.get_key(user_id))


class IsMemberStore(object):
    key_prefix = 'is_member_'

    @staticmethod
    def get_key(user_id):
        return IsMemberStore.key_prefix + str(user_id)

    @staticmethod
    def get(user_id):
        data = redisConn.get(IsMemberStore.get_key(user_id))
        if data is not None:
            return data == b'1'
        return None

    # val "1" or "0"
    @staticmethod
    def set(user_id, val):
        # 10 minutes
        expire = 600
        return redisConn.setex(IsMemberStore.get_key(user_id), expire, '1' if val is True else '0')
