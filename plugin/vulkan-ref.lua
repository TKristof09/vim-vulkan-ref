local create_command = vim.api.nvim_create_user_command

create_command("OpenRefPage", function()
    local w = vim.fn.escape(vim.fn.expand('<cword>'), [[\/]])
    local base_url = "https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/"


    os.execute("start " .. base_url .. w .. ".html")
end, {})
