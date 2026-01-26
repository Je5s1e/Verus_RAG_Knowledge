<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module prelude Copy item path

<span class="sub-heading"><a href="../../src/vstd/prelude.rs.html#1-85" class="src">Source</a>
</span>

</div>

## Re-exports<a href="#reexports" class="anchor">§</a>

`pub use super::map::`<a href="../map/struct.Map.html" class="struct"
title="struct vstd::map::Map"><code>Map</code></a>`;`

`pub use super::map::`<a href="../macro.map.html" class="macro"
title="macro vstd::map"><code>map</code></a>`;`

`pub use super::seq::`<a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq"><code>Seq</code></a>`;`

`pub use super::seq::`<a href="../macro.seq.html" class="macro"
title="macro vstd::seq"><code>seq</code></a>`;`

`pub use super::set::`<a href="../set/struct.Set.html" class="struct"
title="struct vstd::set::Set"><code>Set</code></a>`;`

`pub use super::set::`<a href="../macro.set.html" class="macro"
title="macro vstd::set"><code>set</code></a>`;`

`pub use super::array::`<a href="../array/trait.ArrayAdditionalExecFns.html" class="trait"
title="trait vstd::array::ArrayAdditionalExecFns"><code>ArrayAdditionalExecFns</code></a>`;`

`pub use super::array::`<a href="../array/trait.ArrayAdditionalSpecFns.html" class="trait"
title="trait vstd::array::ArrayAdditionalSpecFns"><code>ArrayAdditionalSpecFns</code></a>`;`

`pub use super::slice::`<a href="../slice/trait.SliceAdditionalSpecFns.html" class="trait"
title="trait vstd::slice::SliceAdditionalSpecFns"><code>SliceAdditionalSpecFns</code></a>`;`

`pub use super::pervasive::`<a href="../pervasive/trait.VecAdditionalExecFns.html" class="trait"
title="trait vstd::pervasive::VecAdditionalExecFns"><code>VecAdditionalExecFns</code></a>`;`

`pub use super::string::`<a href="../string/trait.StrSliceExecFns.html" class="trait"
title="trait vstd::string::StrSliceExecFns"><code>StrSliceExecFns</code></a>`;`

`pub use super::string::`<a href="../string/trait.StringExecFns.html" class="trait"
title="trait vstd::string::StringExecFns"><code>StringExecFns</code></a>`;`

`pub use super::string::`<a href="../string/trait.StringExecFnsIsAscii.html" class="trait"
title="trait vstd::string::StringExecFnsIsAscii"><code>StringExecFnsIsAscii</code></a>`;`

`pub use super::`<a href="../view/index.html" class="mod"
title="mod vstd::view"><code>view</code></a>`::*;`

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.atomic_with_ghost_helper.html" class="macro"
title="macro vstd::prelude::atomic_with_ghost_helper">atomic_with_ghost_helper</a>

<a href="macro.calc_proc_macro.html" class="macro"
title="macro vstd::prelude::calc_proc_macro">calc_proc_macro</a>

<a href="macro.decreases_to.html" class="macro"
title="macro vstd::prelude::decreases_to">decreases_to</a>

decreases_to!(b =\> a) means that height(a) \< height(b), so that b can
decrease to a in decreases clauses. decreases_to!(b1, …, bn =\> a1, …,
am) can compare lexicographically ordered values, which can be useful
when making assertions about decreases clauses. Notes:

<a href="macro.decreases_to_internal.html" class="macro"
title="macro vstd::prelude::decreases_to_internal">decreases_to_internal</a>

<a href="macro.fndecl.html" class="macro"
title="macro vstd::prelude::fndecl">fndecl</a>

<a href="macro.proof.html" class="macro"
title="macro vstd::prelude::proof">proof</a>

Add a verus proof block.

<a href="macro.proof_decl.html" class="macro"
title="macro vstd::prelude::proof_decl">proof_decl</a>

proof_decl add extra stmts that are used only for verification. For
example, declare a ghost/tracked variable. To avoid confusion, let stmts
without ghost/tracked is not supported. Non-local stmts inside
proof_decl! are treated similar to those in proof!

<a href="macro.proof_with.html" class="macro"
title="macro vstd::prelude::proof_with">proof_with</a>

proof_with add ghost input/output to the next function call. In stable
rust, we cannot add attribute-based macro to expr/statement. Using
proof_with! to tell \#\[verus_spec\] to add ghost input/output. Using
proof_with outside of \#\[verus_spec\] does not have any side effects.

<a href="macro.struct_with_invariants.html" class="macro"
title="macro vstd::prelude::struct_with_invariants">struct_with_invariants</a>

<a href="macro.verus.html" class="macro"
title="macro vstd::prelude::verus">verus</a>

<a href="macro.verus_erase_ghost.html" class="macro"
title="macro vstd::prelude::verus_erase_ghost">verus_erase_ghost</a>

<a href="macro.verus_exec_expr.html" class="macro"
title="macro vstd::prelude::verus_exec_expr">verus_exec_expr</a>

<a href="macro.verus_exec_expr_erase_ghost.html" class="macro"
title="macro vstd::prelude::verus_exec_expr_erase_ghost">verus_exec_expr_erase_ghost</a>

<a href="macro.verus_exec_expr_keep_ghost.html" class="macro"
title="macro vstd::prelude::verus_exec_expr_keep_ghost">verus_exec_expr_keep_ghost</a>

<a href="macro.verus_exec_inv_macro_exprs.html" class="macro"
title="macro vstd::prelude::verus_exec_inv_macro_exprs">verus_exec_inv_macro_exprs</a>

<a href="macro.verus_exec_macro_exprs.html" class="macro"
title="macro vstd::prelude::verus_exec_macro_exprs">verus_exec_macro_exprs</a>

<a href="macro.verus_ghost_inv_macro_exprs.html" class="macro"
title="macro vstd::prelude::verus_ghost_inv_macro_exprs">verus_ghost_inv_macro_exprs</a>

<a href="macro.verus_impl.html" class="macro"
title="macro vstd::prelude::verus_impl">verus_impl</a>

Like verus!, but for use inside a (non-trait) impl

<a href="macro.verus_keep_ghost.html" class="macro"
title="macro vstd::prelude::verus_keep_ghost">verus_keep_ghost</a>

<a href="macro.verus_proof_expr.html" class="macro"
title="macro vstd::prelude::verus_proof_expr">verus_proof_expr</a>

<a href="macro.verus_proof_macro_explicit_exprs.html" class="macro"
title="macro vstd::prelude::verus_proof_macro_explicit_exprs">verus_proof_macro_explicit_exprs</a>

`verus_proof_macro_explicit_exprs!(f!(tts))` applies verus syntax to
transform `tts` into `tts'`, then returns `f!(tts')`, only applying the
transform to any of the exprs within it that are explicitly prefixed
with `@@`, leaving the rest as-is. Contrast this to
\[`verus_proof_macro_exprs`\] which is likely what you want to try first
to see if it satisfies your needs.

<a href="macro.verus_proof_macro_exprs.html" class="macro"
title="macro vstd::prelude::verus_proof_macro_exprs">verus_proof_macro_exprs</a>

verus_proof_macro_exprs!(f!(exprs)) applies verus syntax to transform
exprs into exprs’, then returns f!(exprs’), where exprs is a sequence of
expressions separated by “,”, “;”, and/or “=\>”.

<a href="macro.verus_trait_impl.html" class="macro"
title="macro vstd::prelude::verus_trait_impl">verus_trait_impl</a>

Like verus!, but for use inside a trait impl

<a href="macro.with_triggers.html" class="macro"
title="macro vstd::prelude::with_triggers">with_triggers</a>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.FnProof.html" class="struct"
title="struct vstd::prelude::FnProof">FnProof</a>

FnProof is the type of proof closures; the syntax proof_fn is used to
wrap FnProof

<a href="struct.FnSpec.html" class="struct"
title="struct vstd::prelude::FnSpec">FnSpec</a>

<a href="struct.Ghost.html" class="struct"
title="struct vstd::prelude::Ghost">Ghost</a>

<a href="struct.NoCopy.html" class="struct"
title="struct vstd::prelude::NoCopy">NoCopy</a>

<a href="struct.ProofFnConfirm.html" class="struct"
title="struct vstd::prelude::ProofFnConfirm">ProofFnConfirm</a>

<a href="struct.SpecChain.html" class="struct"
title="struct vstd::prelude::SpecChain">SpecChain</a>

<a href="struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>

<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

<a href="struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

<a href="struct.real.html" class="struct"
title="struct vstd::prelude::real">real</a>

## Constants<a href="#constants" class="anchor">§</a>

<a href="constant.PROOF_FN.html" class="constant"
title="constant vstd::prelude::PROOF_FN">PROOF_FN</a>

<a href="constant.PROOF_FN_COPY.html" class="constant"
title="constant vstd::prelude::PROOF_FN_COPY">PROOF_FN_COPY</a>

<a href="constant.PROOF_FN_MUT.html" class="constant"
title="constant vstd::prelude::PROOF_FN_MUT">PROOF_FN_MUT</a>

<a href="constant.PROOF_FN_ONCE.html" class="constant"
title="constant vstd::prelude::PROOF_FN_ONCE">PROOF_FN_ONCE</a>

<a href="constant.PROOF_FN_SEND.html" class="constant"
title="constant vstd::prelude::PROOF_FN_SEND">PROOF_FN_SEND</a>

<a href="constant.PROOF_FN_SYNC.html" class="constant"
title="constant vstd::prelude::PROOF_FN_SYNC">PROOF_FN_SYNC</a>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Boolean.html" class="trait"
title="trait vstd::prelude::Boolean">Boolean</a>  
<a href="trait.Chainable.html" class="trait"
title="trait vstd::prelude::Chainable">Chainable</a>  
<a href="trait.Decimal.html" class="trait"
title="trait vstd::prelude::Decimal">Decimal</a>  
<a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>  
<a href="trait.ProofFn.html" class="trait"
title="trait vstd::prelude::ProofFn">ProofFn</a>  
<a href="trait.ProofFnMut.html" class="trait"
title="trait vstd::prelude::ProofFnMut">ProofFnMut</a>  
<a href="trait.ProofFnOnce.html" class="trait"
title="trait vstd::prelude::ProofFnOnce">ProofFnOnce</a>  
<a href="trait.ProofFnReqEns.html" class="trait"
title="trait vstd::prelude::ProofFnReqEns">ProofFnReqEns</a>  
<a href="trait.ProofFnReqEnsDef.html" class="trait"
title="trait vstd::prelude::ProofFnReqEnsDef">ProofFnReqEnsDef</a>  
<a href="trait.SpecAdd.html" class="trait"
title="trait vstd::prelude::SpecAdd">SpecAdd</a>  
<a href="trait.SpecBitAnd.html" class="trait"
title="trait vstd::prelude::SpecBitAnd">SpecBitAnd</a>  
<a href="trait.SpecBitOr.html" class="trait"
title="trait vstd::prelude::SpecBitOr">SpecBitOr</a>  
<a href="trait.SpecBitXor.html" class="trait"
title="trait vstd::prelude::SpecBitXor">SpecBitXor</a>  
<a href="trait.SpecEuclideanMod.html" class="trait"
title="trait vstd::prelude::SpecEuclideanMod">SpecEuclideanMod</a>  
<a href="trait.SpecEuclideanOrRealDiv.html" class="trait"
title="trait vstd::prelude::SpecEuclideanOrRealDiv">SpecEuclideanOrRealDiv</a>  
<a href="trait.SpecMul.html" class="trait"
title="trait vstd::prelude::SpecMul">SpecMul</a>  
<a href="trait.SpecNeg.html" class="trait"
title="trait vstd::prelude::SpecNeg">SpecNeg</a>  
<a href="trait.SpecOrd.html" class="trait"
title="trait vstd::prelude::SpecOrd">SpecOrd</a>  
<a href="trait.SpecShl.html" class="trait"
title="trait vstd::prelude::SpecShl">SpecShl</a>  
<a href="trait.SpecShr.html" class="trait"
title="trait vstd::prelude::SpecShr">SpecShr</a>  
<a href="trait.SpecSub.html" class="trait"
title="trait vstd::prelude::SpecSub">SpecSub</a>  
<a href="trait.Structural.html" class="trait"
title="trait vstd::prelude::Structural">Structural</a>  
derive(Structural) means that exec-mode == and ghost == always yield the
same result. derive(Structural) is only allowed when all the fields of a
type are also Structural. derive(StructuralEq) means derive(Structural)
and also implement PartialEqSpec, setting eq_spec to == and
obeys_eq_spec to true.

## Attribute Macros<a href="#attributes" class="anchor">§</a>

<a href="attr.is_variant.html" class="attr"
title="attr vstd::prelude::is_variant">is_variant</a>

Add `is_<VARIANT>` and `get_<VARIANT>` functions to an enum

<a href="attr.is_variant_no_deprecation_warning.html" class="attr"
title="attr vstd::prelude::is_variant_no_deprecation_warning">is_variant_no_deprecation_warning</a>

Add `is_<VARIANT>` and `get_<VARIANT>` functions to an enum

<a href="attr.verus_enum_synthesize.html" class="attr"
title="attr vstd::prelude::verus_enum_synthesize">verus_enum_synthesize</a>

<a href="attr.verus_spec.html" class="attr"
title="attr vstd::prelude::verus_spec">verus_spec</a>

<a href="attr.verus_verify.html" class="attr"
title="attr vstd::prelude::verus_verify">verus_verify</a>

## Derive Macros<a href="#derives" class="anchor">§</a>

<a href="derive.Structural.html" class="derive"
title="derive vstd::prelude::Structural">Structural</a>

<a href="derive.StructuralEq.html" class="derive"
title="derive vstd::prelude::StructuralEq">StructuralEq</a>

</div>

</div>
