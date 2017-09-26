#include "stdafx.h"
#include "CppUnitTest.h"
#include <vector>
#include <iostream>
#include <string>
#include "joiner.hpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace joiner
{		
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
      std::string joined = joiner::join(std::vector<int>({ 1, 2, 3, 4, 5 }), ",");
      Logger::WriteMessage(joined.c_str());
		}

	};
}