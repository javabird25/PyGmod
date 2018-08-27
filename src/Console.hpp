#pragma once

#include "GarrysMod/Lua/Interface.h"
#include <string>

using namespace GarrysMod::Lua;
using std::string;

// Provides printing and logging functionality to Garry's Mod console.
class Console {
public:
	Console(ILuaBase *lua) : lua(lua) {};

	// string overloads

	// Prints message to the console.
	void println(string message);

	// Prints "[GPython] " + message to the console.
	void log(string message);

	// Prints "[GPython] ERROR: " + message to the console.
	void error(string message);

	// Prints "[GPython] WARN: " + message to the console.
	void warn(string message);

	// const char* overloads

	// Prints message to the console.
	void println(const char* message);

	// Prints "[GPython] " + message to the console.
	void log(const char* message);

	// Prints "[GPython] ERROR: " + message to the console.
	void error(const char* message);

	// Prints "[GPython] WARNING: " + message to the console.
	void warn(const char* message);

	// int overloads

	// Prints message to the console.
	void println(int message);

	// Prints "[GPython] " + message to the console.
	void log(int message);

	// Prints "[GPython] ERROR: " + message to the console.
	void error(int message);

	// Prints "[GPython] WARNING: " + message to the console.
	void warn(int message);

private:
	ILuaBase *lua;
};
