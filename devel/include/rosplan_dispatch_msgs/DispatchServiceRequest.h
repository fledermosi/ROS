// Generated by gencpp from file rosplan_dispatch_msgs/DispatchServiceRequest.msg
// DO NOT EDIT!


#ifndef ROSPLAN_DISPATCH_MSGS_MESSAGE_DISPATCHSERVICEREQUEST_H
#define ROSPLAN_DISPATCH_MSGS_MESSAGE_DISPATCHSERVICEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rosplan_dispatch_msgs
{
template <class ContainerAllocator>
struct DispatchServiceRequest_
{
  typedef DispatchServiceRequest_<ContainerAllocator> Type;

  DispatchServiceRequest_()
    {
    }
  DispatchServiceRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> const> ConstPtr;

}; // struct DispatchServiceRequest_

typedef ::rosplan_dispatch_msgs::DispatchServiceRequest_<std::allocator<void> > DispatchServiceRequest;

typedef boost::shared_ptr< ::rosplan_dispatch_msgs::DispatchServiceRequest > DispatchServiceRequestPtr;
typedef boost::shared_ptr< ::rosplan_dispatch_msgs::DispatchServiceRequest const> DispatchServiceRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace rosplan_dispatch_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosplan_dispatch_msgs/DispatchServiceRequest";
  }

  static const char* value(const ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DispatchServiceRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::rosplan_dispatch_msgs::DispatchServiceRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ROSPLAN_DISPATCH_MSGS_MESSAGE_DISPATCHSERVICEREQUEST_H
