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

let g:vim_vulkan_ref_plugin_loaded = 1

function! OpenRefPage()
  python3 open_ref_page()
endfunction

command! -nargs=0 OpenRefPage call OpenRefPage()