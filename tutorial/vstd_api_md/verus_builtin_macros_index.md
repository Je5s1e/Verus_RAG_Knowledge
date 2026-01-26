<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate verus_builtin_macros Copy item path

<span class="sub-heading"><a href="../src/verus_builtin_macros/lib.rs.html#1-454"
class="src">Source</a> </span>

</div>

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.atomic_with_ghost_helper.html" class="macro"
title="macro verus_builtin_macros::atomic_with_ghost_helper">atomic_with_ghost_helper</a>  
<a href="macro.calc_proc_macro.html" class="macro"
title="macro verus_builtin_macros::calc_proc_macro">calc_proc_macro</a>  
<a href="macro.exec_spec.html" class="macro"
title="macro verus_builtin_macros::exec_spec">exec_spec</a>  
Automatically compiles spec items to exec items, with proofs of
functional correctness.

<a href="macro.fndecl.html" class="macro"
title="macro verus_builtin_macros::fndecl">fndecl</a>  
<a href="macro.proof.html" class="macro"
title="macro verus_builtin_macros::proof">proof</a>  
Add a verus proof block.

<a href="macro.proof_decl.html" class="macro"
title="macro verus_builtin_macros::proof_decl">proof_decl</a>  
proof_decl add extra stmts that are used only for verification. For
example, declare a ghost/tracked variable. To avoid confusion, let stmts
without ghost/tracked is not supported. Non-local stmts inside
proof_decl! are treated similar to those in proof!

<a href="macro.proof_with.html" class="macro"
title="macro verus_builtin_macros::proof_with">proof_with</a>  
proof_with add ghost input/output to the next function call. In stable
rust, we cannot add attribute-based macro to expr/statement. Using
proof_with! to tell
\#[verus_spec](attr.verus_spec.html "attr verus_builtin_macros::verus_spec")
to add ghost input/output. Using proof_with outside of
\#[verus_spec](attr.verus_spec.html "attr verus_builtin_macros::verus_spec")
does not have any side effects.

<a href="macro.struct_with_invariants.html" class="macro"
title="macro verus_builtin_macros::struct_with_invariants">struct_with_invariants</a>  
<a href="macro.verus.html" class="macro"
title="macro verus_builtin_macros::verus">verus</a>  
<a href="macro.verus_erase_ghost.html" class="macro"
title="macro verus_builtin_macros::verus_erase_ghost">verus_erase_ghost</a>  
<a href="macro.verus_exec_expr.html" class="macro"
title="macro verus_builtin_macros::verus_exec_expr">verus_exec_expr</a>  
<a href="macro.verus_exec_expr_erase_ghost.html" class="macro"
title="macro verus_builtin_macros::verus_exec_expr_erase_ghost">verus_exec_expr_erase_ghost</a>  
<a href="macro.verus_exec_expr_keep_ghost.html" class="macro"
title="macro verus_builtin_macros::verus_exec_expr_keep_ghost">verus_exec_expr_keep_ghost</a>  
<a href="macro.verus_exec_inv_macro_exprs.html" class="macro"
title="macro verus_builtin_macros::verus_exec_inv_macro_exprs">verus_exec_inv_macro_exprs</a>  
<a href="macro.verus_exec_macro_exprs.html" class="macro"
title="macro verus_builtin_macros::verus_exec_macro_exprs">verus_exec_macro_exprs</a>  
<a href="macro.verus_ghost_inv_macro_exprs.html" class="macro"
title="macro verus_builtin_macros::verus_ghost_inv_macro_exprs">verus_ghost_inv_macro_exprs</a>  
<a href="macro.verus_impl.html" class="macro"
title="macro verus_builtin_macros::verus_impl">verus_impl</a>  
Like verus!, but for use inside a (non-trait) impl

<a href="macro.verus_keep_ghost.html" class="macro"
title="macro verus_builtin_macros::verus_keep_ghost">verus_keep_ghost</a>  
<a href="macro.verus_proof_expr.html" class="macro"
title="macro verus_builtin_macros::verus_proof_expr">verus_proof_expr</a>  
<a href="macro.verus_proof_macro_explicit_exprs.html" class="macro"
title="macro verus_builtin_macros::verus_proof_macro_explicit_exprs">verus_proof_macro_explicit_exprs</a>  
`verus_proof_macro_explicit_exprs!(f!(tts))` applies verus syntax to
transform `tts` into `tts'`, then returns `f!(tts')`, only applying the
transform to any of the exprs within it that are explicitly prefixed
with `@@`, leaving the rest as-is. Contrast this to
[`verus_proof_macro_exprs`](macro.verus_proof_macro_exprs.html "macro verus_builtin_macros::verus_proof_macro_exprs")
which is likely what you want to try first to see if it satisfies your
needs.

<a href="macro.verus_proof_macro_exprs.html" class="macro"
title="macro verus_builtin_macros::verus_proof_macro_exprs">verus_proof_macro_exprs</a>  
verus_proof_macro_exprs!(f!(exprs)) applies verus syntax to transform
exprs into exprs’, then returns f!(exprs’), where exprs is a sequence of
expressions separated by “,”, “;”, and/or “=\>”.

<a href="macro.verus_trait_impl.html" class="macro"
title="macro verus_builtin_macros::verus_trait_impl">verus_trait_impl</a>  
Like verus!, but for use inside a trait impl

## Attribute Macros<a href="#attributes" class="anchor">§</a>

<a href="attr.auto_spec.html" class="attr"
title="attr verus_builtin_macros::auto_spec">auto_spec</a>

This copies the body of an exec function into a “returns” clause, so
that the exec function will be also usable as a spec function. For
example, `#[vstd::contrib::auto_spec] fn f(u: u8) -> u8 { u / 2 }`
becomes:
`#[verifier::allow_in_spec] fn f(u: u8) -> u8 returns (u / 2) { u / 2 }`
The macro performs some limited fixups, such as removing proof blocks
and turning +, -, and \* into add, sub, mul. However, only a few such
fixups are currently implemented and not all exec bodies will be usable
as return clauses, so this macro will not work on all exec functions.

<a href="attr.is_variant.html" class="attr"
title="attr verus_builtin_macros::is_variant">is_variant</a>

Add `is_<VARIANT>` and `get_<VARIANT>` functions to an enum

<a href="attr.is_variant_no_deprecation_warning.html" class="attr"
title="attr verus_builtin_macros::is_variant_no_deprecation_warning">is_variant_no_deprecation_warning</a>

Add `is_<VARIANT>` and `get_<VARIANT>` functions to an enum

<a href="attr.verus_enum_synthesize.html" class="attr"
title="attr verus_builtin_macros::verus_enum_synthesize">verus_enum_synthesize</a>

<a href="attr.verus_spec.html" class="attr"
title="attr verus_builtin_macros::verus_spec">verus_spec</a>

<a href="attr.verus_verify.html" class="attr"
title="attr verus_builtin_macros::verus_verify">verus_verify</a>

## Derive Macros<a href="#derives" class="anchor">§</a>

<a href="derive.Structural.html" class="derive"
title="derive verus_builtin_macros::Structural">Structural</a>

<a href="derive.StructuralEq.html" class="derive"
title="derive verus_builtin_macros::StructuralEq">StructuralEq</a>

</div>

</div>
