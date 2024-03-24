lua_code = """--- This is a Lua Script
function test_function()
    local message = "Hello from Lua!"
    print(message)
end
"""

lua_file_path = 'example.lua'

with open(lua_file_path, "w") as lua_file:
    lua_file.write(lua_code)

print(f'Lua code has been written to {lua_file_path}')