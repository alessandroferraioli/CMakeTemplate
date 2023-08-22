#include <gtest/gtest.h>
#include <string>



TEST(CheckTest,fail_test)
{
   std::string rhs = "test001";
   std::string lhs = "test1";

   ASSERT_NE(rhs,lhs);
   rhs = lhs;
   ASSERT_EQ(rhs,lhs);
}