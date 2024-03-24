-- Read the result from the file
local file = io.open("result.txt", "r")
local result_str = file:read("*all")
file:close()

-- Convert the result to a number
local result = tonumber(result_str)

-- Use the result in your Lua program (e.g., print it)
print("Result from Python:", result)