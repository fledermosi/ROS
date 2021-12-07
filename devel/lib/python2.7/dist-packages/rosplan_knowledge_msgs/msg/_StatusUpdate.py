# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rosplan_knowledge_msgs/StatusUpdate.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class StatusUpdate(genpy.Message):
  _md5sum = "184cadf1052e240c262af1a764339990"
  _type = "rosplan_knowledge_msgs/StatusUpdate"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# A message used to publish a status notification from the Knowledge Base
# This status notifies that the KB has been updated.

string last_update_client
time last_update_time

"""
  __slots__ = ['last_update_client','last_update_time']
  _slot_types = ['string','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       last_update_client,last_update_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StatusUpdate, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.last_update_client is None:
        self.last_update_client = ''
      if self.last_update_time is None:
        self.last_update_time = genpy.Time()
    else:
      self.last_update_client = ''
      self.last_update_time = genpy.Time()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.last_update_client
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.last_update_time.secs, _x.last_update_time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.last_update_time is None:
        self.last_update_time = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.last_update_client = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.last_update_client = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.last_update_time.secs, _x.last_update_time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.last_update_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.last_update_client
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.last_update_time.secs, _x.last_update_time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.last_update_time is None:
        self.last_update_time = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.last_update_client = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.last_update_client = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.last_update_time.secs, _x.last_update_time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.last_update_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
