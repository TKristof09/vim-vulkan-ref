if exists('g:vim_vulkan_ref_plugin_loaded')
  finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import vim_vulkan_ref
EOF

let g:vim_vulkan_ref_plugin_loaded = 1

function! StartDriver()
    python3 vim_vulkan_ref.start_driver()
endfunction

function! OpenRefPage()
  python3 vim_vulkan_ref.open_ref_page()
endfunction

function! CloseDriver()
    python3 vim_vulkan_ref.close_driver()
endfunction

command! -nargs=0 OpenRefPage call OpenRefPage()
command! -nargs=0 StartDriver call StartDriver()
command! -nargs=0 CloseDriver call CloseDriver()

