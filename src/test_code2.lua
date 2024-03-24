-- add a custom directory to package.path
-- package.cpath = package.cpath .. ";C:\\Users\\danie\\AppData\\Roaming\\luarocks\\lib\\lua\\5.4\\lfs.dll"

local lfs = require("lfs")

print("LuaFileSystem loaded succesfully!")

-- local new_directory = "my_new_folder"
local success, err = lfs.currentdir()

if success then
    print("Current Working Directory:", success)
else
    print("Error creating directory:", err)
end