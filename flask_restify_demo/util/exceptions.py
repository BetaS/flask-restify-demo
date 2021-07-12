# -*- coding: utf-8 -*-


class BadParameter(Exception):
    pass


class NoDataException(Exception):
    pass


class NoPermissionException(Exception):
    pass


class NotFoundException(Exception):
    pass


class InvalidStatusException(Exception):
    pass


class PrerequisiteNotMatchException(Exception):
    """Error when prerequisite status does not matched"""
    pass


class AlreadyExistException(Exception):
    """Error when given email is already exist"""
    pass


class MalformedException(Exception):
    """Error when given password is malformed"""
    pass


class RequirementNotMatchException(Exception):
    """Error when requirement does not matched"""
    pass


class TimeoutException(Exception):
    """Error when request timeout"""
    pass
