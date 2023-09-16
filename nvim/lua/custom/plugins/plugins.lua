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
        "lervag/vimtex" --VimTeX
    },
    {
        'edKotinsky/Arduino.nvim' -- Arduino LSP
    },
    {
        'phaazon/hop.nvim', -- motions
        branch = 'v2',
        config = function ()
            require'hop'.setup ()
            local hop = require('hop')
            local directions = require('hop.hint').HintDirection
            vim.keymap.set('', 'f', function()
              hop.hint_char1({ direction = directions.AFTER_CURSOR, current_line_only = true })
            end, {remap=true})
            vim.keymap.set('', 'F', function()
              hop.hint_char1({ direction = directions.BEFORE_CURSOR, current_line_only = true })
            end, {remap=true})
            vim.keymap.set('', 't', function()
              hop.hint_char1({ direction = directions.AFTER_CURSOR, current_line_only = true, hint_offset = -1 })
            end, {remap=true})
            vim.keymap.set('', 'T', function()
              hop.hint_char1({ direction = directions.BEFORE_CURSOR, current_line_only = true, hint_offset = 1 })
            end, {remap=true})
        end
    },
    { -- This plugin
      "Zeioth/compiler.nvim",
      cmd = {"CompilerOpen", "CompilerToggleResults", "CompilerRedo"},
      dependencies = { "stevearc/overseer.nvim" },
      opts = {},
    },
    { -- The task runner we use
      "stevearc/overseer.nvim",
      commit = "19aac0426710c8fc0510e54b7a6466a03a1a7377",
      cmd = { "CompilerOpen", "CompilerToggleResults", "CompilerRedo" },
      opts = {
        task_list = {
          direction = "bottom",
          min_height = 25,
          max_height = 25,
          default_detail = 1,
          bindings = { ["q"] = function() vim.cmd("OverseerClose") end },
        },
      },
    },
    {
       'mhartington/formatter.nvim'
    },
}
