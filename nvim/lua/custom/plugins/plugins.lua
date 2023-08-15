-- You can add your own plugins here or in other files in this directory!
--  I promise not to create any merge conflicts in this directory :)
--
-- See the kickstart.nvim README for more information
return {
    {
        'goolord/alpha-nvim',
        event = "VimEnter",
        dependencies = { 'nvim-tree/nvim-web-devicons' },
        config = function ()
            require'alpha'.setup(require'alpha.themes.dashboard'.config)
            local alpha = require("alpha")
            local dashboard = require("alpha.themes.dashboard")
                        -- Set header
            dashboard.section.header.val = {
                    "                                                                    ",
                    "      ████ ██████           █████      ██                     ",
                    "     ███████████             █████                             ",
                    "     █████████ ███████████████████ ███   ███████████   ",
                    "    █████████  ███    █████████████ █████ ██████████████   ",
                    "   █████████ ██████████ █████████ █████ █████ ████ █████   ",
                    " ███████████ ███    ███ █████████ █████ █████ ████ █████  ",
                    "██████  █████████████████████ ████ █████ █████ ████ ██████ ",
            }
        end,
    },
    {
        'psliwka/vim-smoothie' -- Scroll smoothing
    },
    {
        "kylechui/nvim-surround", -- Quickly surround code with bracket etc
        version = "*", -- Use for stability; omit to use `main` branch for the latest features
        event = "VeryLazy",
        config = function()
            require("nvim-surround").setup()
        end
    },
    {
        'rstacruz/vim-closer' -- Vim bracket closer on enter
    },
    {
        'codota/tabnine-nvim', -- Tabnine autocomplete
        build = "./dl_binaries.sh",
        config = function()
            require('tabnine.status').status()
            require('tabnine').setup({
                disable_auto_comment=true,
                accept_keymap="<Tab>",
                dismiss_keymap = "<C-]>",
                debounce_ms = 800,
                suggestion_color = {gui = "#808080", cterm = 244},
                exclude_filetypes = {"TelescopePrompt"},
                log_file_path = nil, -- absolute path to Tabnine log file
            })
            require('lualine').setup({
                tabline = {
                    lualine_a = {},
                    lualine_b = {'branch'},
                    lualine_c = {'filename'},
                    lualine_x = {},
                    lualine_y = {},
                    lualine_z = {}
                },
                sections = {lualine_c = {'lsp_progress'}, lualine_x = {'tabnine'}}
            })
        end
    },
}
