from pygments.lexer import words, inherit
from pygments.lexers import CLexer
from pygments.token import *

class SaCLexer(CLexer):
    """
    For Single-Assignment C (SaC) source code with preprocessor directives.
    This makes use of the existing definitions given in the C/C++ Lexers.
    We extend these to include SaC specific stuff.
    """
    name = "Single-Assignment C"
    aliases = ['sac']
    filenames = ['*.sac']
    mimetypes = ['text/plain']

    # builtins
    primitives = ('_dim_A_', '_shape_A_', '_reshape_VxA_', '_sel_VxA_', '_modarray_AxVxS_',
                  '_hideValue_SxA_', '_hideShape_SxA_', '_hideDim_SxA_', '_cat_VxV_',
                  '_take_SxV_', '_drop_SxV_', '_add_SxS_', '_add_SxV_', '_add_VxS_',
                  '_add_VxV_', '_sub_SxS_', '_sub_SxV_', '_sub_VxS_', '_sub_VxV_', '_mul_SxS_',
                  '_mul_SxV_', '_mul_VxS_','_mul_VxV_', '_div_SxS_', '_div_SxV_', '_div_VxS_',
                  '_div_VxV_', '_mod_SxS_', '_mod_SxV_', '_mod_VxS_', '_mod_VxV_', '_min_SxS_'
                  '_min_SxV_', '_min_VxS_', '_min_VxV_', '_max_SxS_', '_max_SxV_', '_max_VxS_',
                  '_max_VxV_', '_abs_S_', '_abs_V_', '_neg_S_', '_neg_V_', '_reciproc_S_',
                  '_reciproc_V_', '_mesh_VxVxV_', '_eq_SxS_', '_eq_SxV_', '_eq_VxS_', '_eq_VxV_',
                  '_neq_SxS_', '_neq_SxV_', '_neq_VxS_', '_neq_VxV_', '_le_SxS_', '_le_SxV_',
                  '_le_VxS_', '_le_VxV_', '_lt_SxS_', '_lt_SxV_', '_lt_VxS_', '_lt_VxV_',
                  '_ge_SxS_', '_ge_SxV_', '_ge_VxS_', '_ge_VxV_', '_gt_SxS_', '_gt_SxV_', '_gt_VxS_',
                  '_gt_VxV_', '_and_SxS_', '_and_SxV_', '_and_VxS_', '_and_VxV_', '_or_SxS_',
                  '_or_SxV_', '_or_VxS_', '_or_VxV_', '_not_S_', '_not_V_', '_tob_S_', '_tos_S_',
                  '_toi_S_', '_tol_S_', '_toll_S_', '_toub_S_', '_tous_S_', '_toui_S_', '_toul_S_',
                  '_toull_S_', '_tof_S_', '_tod_S_', '_toc_S_', '_tobool_S_')

    # automatically merges with inherited `tokens`.
    tokens = {
        'statements': [
            (r'(with|modarray|genarray|fold|foldfix|propogate)', Keyword),
            (r'(noinline|specialize|use|import|provide|export|all|module|step|width|builtin|external|typerel|objdef)', Keyword.Reserved),
            (r'\.', Operator),
            (words(primitives, suffix=r'\b'), Name.Builtin),
            inherit,
        ]
    }
