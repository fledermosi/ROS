# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rosplan_dispatch_msgs/PlanGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PlanGoal(genpy.Message):
  _md5sum = "ec56e034bdab5d47c02286cf335fd906"
  _type = "rosplan_dispatch_msgs/PlanGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Planning action definition
# goal definition
string domain_path
string problem_path
string data_path
string planner_command
bool use_problem_topic
uint64 start_action_id
"""
  __slots__ = ['domain_path','problem_path','data_path','planner_command','use_problem_topic','start_action_id']
  _slot_types = ['string','string','string','string','bool','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       domain_path,problem_path,data_path,planner_command,use_problem_topic,start_action_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.domain_path is None:
        self.domain_path = ''
      if self.problem_path is None:
        self.problem_path = ''
      if self.data_path is None:
        self.data_path = ''
      if self.planner_command is None:
        self.planner_command = ''
      if self.use_problem_topic is None:
        self.use_problem_topic = False
      if self.start_action_id is None:
        self.start_action_id = 0
    else:
      self.domain_path = ''
      self.problem_path = ''
      self.data_path = ''
      self.planner_command = ''
      self.use_problem_topic = False
      self.start_action_id = 0

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
      _x = self.domain_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.problem_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.data_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.planner_command
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BQ().pack(_x.use_problem_topic, _x.start_action_id))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.domain_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.domain_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.problem_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.problem_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.data_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_command = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planner_command = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.use_problem_topic, _x.start_action_id,) = _get_struct_BQ().unpack(str[start:end])
      self.use_problem_topic = bool(self.use_problem_topic)
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
      _x = self.domain_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.problem_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.data_path
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.planner_command
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BQ().pack(_x.use_problem_topic, _x.start_action_id))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.domain_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.domain_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.problem_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.problem_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data_path = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.data_path = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_command = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planner_command = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.use_problem_topic, _x.start_action_id,) = _get_struct_BQ().unpack(str[start:end])
      self.use_problem_topic = bool(self.use_problem_topic)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BQ = None
def _get_struct_BQ():
    global _struct_BQ
    if _struct_BQ is None:
        _struct_BQ = struct.Struct("<BQ")
    return _struct_BQ
