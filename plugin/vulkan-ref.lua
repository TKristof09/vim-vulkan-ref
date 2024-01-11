local create_command = vim.api.nvim_create_user_command

create_command("OpenRefPage", function()
    local w = vim.fn.escape(vim.fn.expand('<cword>'), [[\/]])
    local base_url_vulkan = "https://www.khronos.org/registry/vulkan/specs/1.3-extensions/man/html/"
    local base_url_glsl = "https://registry.khronos.org/OpenGL-Refpages/gl4/html/"


    if vim.bo.filetype == "glsl" then
        os.execute("start " .. base_url_glsl .. w .. ".xhtml")
    else
        os.execute("start " .. base_url_vulkan .. w .. ".html")
    end
end, {})
