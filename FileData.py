import json


class File:

    def __init__(self, file_name, is_antlr_file, enter_cnt, exit_cnt, visit_cnt):

        self._file_name = file_name
        self._is_antlr_file = is_antlr_file
        self._enter_cnt = enter_cnt
        self._exit_cnt = exit_cnt
        self._visit_cnt = visit_cnt

    @classmethod
    def from_json_file(cls, json_data):
        cls_dict = json.loads(json_data)
        return cls(cls_dict['_file_name'], cls_dict['_is_antlr_file'], cls_dict['_enter_cnt'], cls_dict['_exit_cnt'], cls_dict['_visit_cnt'])

    def get_file_name(self):
        return self._file_name

    def get_is_antlr_file(self):
        return self._is_antlr_file

    def get_enter_cnt(self):
        return self._enter_cnt

    def get_exit_cnt(self):
        return self._exit_cnt

    def get_visit_cnt(self):
        return self._visit_cnt

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def __repr__(self):
        return self.toJson()
