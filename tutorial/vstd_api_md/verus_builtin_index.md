<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate verus_builtin Copy item path

<span class="sub-heading"><a href="../src/verus_builtin/lib.rs.html#1-1982" class="src">Source</a>
</span>

</div>

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.decreases_to.html" class="macro"
title="macro verus_builtin::decreases_to">decreases_to</a>

decreases_to!(b =\> a) means that height(a) \< height(b), so that b can
decrease to a in decreases clauses. decreases_to!(b1, …, bn =\> a1, …,
am) can compare lexicographically ordered values, which can be useful
when making assertions about decreases clauses. Notes:

<a href="macro.decreases_to_internal.html" class="macro"
title="macro verus_builtin::decreases_to_internal">decreases_to_internal</a>

<a href="macro.with_triggers.html" class="macro"
title="macro verus_builtin::with_triggers">with_triggers</a>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.FnProof.html" class="struct"
title="struct verus_builtin::FnProof">FnProof</a>

FnProof is the type of proof closures; the syntax proof_fn is used to
wrap FnProof

<a href="struct.FnSpec.html" class="struct"
title="struct verus_builtin::FnSpec">FnSpec</a>

<a href="struct.Ghost.html" class="struct"
title="struct verus_builtin::Ghost">Ghost</a>

<a href="struct.NoCopy.html" class="struct"
title="struct verus_builtin::NoCopy">NoCopy</a>

<a href="struct.ProofFnConfirm.html" class="struct"
title="struct verus_builtin::ProofFnConfirm">ProofFnConfirm</a>

<a href="struct.SpecChain.html" class="struct"
title="struct verus_builtin::SpecChain">SpecChain</a>

<a href="struct.Tracked.html" class="struct"
title="struct verus_builtin::Tracked">Tracked</a>

<a href="struct.int.html" class="struct"
title="struct verus_builtin::int">int</a>

<a href="struct.nat.html" class="struct"
title="struct verus_builtin::nat">nat</a>

<a href="struct.real.html" class="struct"
title="struct verus_builtin::real">real</a>

## Constants<a href="#constants" class="anchor">§</a>

<a href="constant.PROOF_FN.html" class="constant"
title="constant verus_builtin::PROOF_FN">PROOF_FN</a>

<a href="constant.PROOF_FN_COPY.html" class="constant"
title="constant verus_builtin::PROOF_FN_COPY">PROOF_FN_COPY</a>

<a href="constant.PROOF_FN_MUT.html" class="constant"
title="constant verus_builtin::PROOF_FN_MUT">PROOF_FN_MUT</a>

<a href="constant.PROOF_FN_ONCE.html" class="constant"
title="constant verus_builtin::PROOF_FN_ONCE">PROOF_FN_ONCE</a>

<a href="constant.PROOF_FN_SEND.html" class="constant"
title="constant verus_builtin::PROOF_FN_SEND">PROOF_FN_SEND</a>

<a href="constant.PROOF_FN_SYNC.html" class="constant"
title="constant verus_builtin::PROOF_FN_SYNC">PROOF_FN_SYNC</a>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Boolean.html" class="trait"
title="trait verus_builtin::Boolean">Boolean</a>  
<a href="trait.Chainable.html" class="trait"
title="trait verus_builtin::Chainable">Chainable</a>  
<a href="trait.Decimal.html" class="trait"
title="trait verus_builtin::Decimal">Decimal</a>  
<a href="trait.Integer.html" class="trait"
title="trait verus_builtin::Integer">Integer</a>  
<a href="trait.ProofFn.html" class="trait"
title="trait verus_builtin::ProofFn">ProofFn</a>  
<a href="trait.ProofFnMut.html" class="trait"
title="trait verus_builtin::ProofFnMut">ProofFnMut</a>  
<a href="trait.ProofFnOnce.html" class="trait"
title="trait verus_builtin::ProofFnOnce">ProofFnOnce</a>  
<a href="trait.ProofFnReqEns.html" class="trait"
title="trait verus_builtin::ProofFnReqEns">ProofFnReqEns</a>  
<a href="trait.ProofFnReqEnsDef.html" class="trait"
title="trait verus_builtin::ProofFnReqEnsDef">ProofFnReqEnsDef</a>  
<a href="trait.SpecAdd.html" class="trait"
title="trait verus_builtin::SpecAdd">SpecAdd</a>  
<a href="trait.SpecBitAnd.html" class="trait"
title="trait verus_builtin::SpecBitAnd">SpecBitAnd</a>  
<a href="trait.SpecBitOr.html" class="trait"
title="trait verus_builtin::SpecBitOr">SpecBitOr</a>  
<a href="trait.SpecBitXor.html" class="trait"
title="trait verus_builtin::SpecBitXor">SpecBitXor</a>  
<a href="trait.SpecEuclideanMod.html" class="trait"
title="trait verus_builtin::SpecEuclideanMod">SpecEuclideanMod</a>  
<a href="trait.SpecEuclideanOrRealDiv.html" class="trait"
title="trait verus_builtin::SpecEuclideanOrRealDiv">SpecEuclideanOrRealDiv</a>  
<a href="trait.SpecMul.html" class="trait"
title="trait verus_builtin::SpecMul">SpecMul</a>  
<a href="trait.SpecNeg.html" class="trait"
title="trait verus_builtin::SpecNeg">SpecNeg</a>  
<a href="trait.SpecOrd.html" class="trait"
title="trait verus_builtin::SpecOrd">SpecOrd</a>  
<a href="trait.SpecShl.html" class="trait"
title="trait verus_builtin::SpecShl">SpecShl</a>  
<a href="trait.SpecShr.html" class="trait"
title="trait verus_builtin::SpecShr">SpecShr</a>  
<a href="trait.SpecSub.html" class="trait"
title="trait verus_builtin::SpecSub">SpecSub</a>  
<a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a>  
derive(Structural) means that exec-mode == and ghost == always yield the
same result. derive(Structural) is only allowed when all the fields of a
type are also Structural. derive(StructuralEq) means derive(Structural)
and also implement PartialEqSpec, setting eq_spec to == and
obeys_eq_spec to true.

</div>

</div>
