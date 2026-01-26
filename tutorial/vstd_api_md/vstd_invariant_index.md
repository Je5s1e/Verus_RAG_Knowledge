<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module invariant Copy item path

<span class="sub-heading"><a href="../../src/vstd/invariant.rs.html#1-599" class="src">Source</a>
</span>

</div>

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.open_atomic_invariant.html" class="macro"
title="macro vstd::invariant::open_atomic_invariant">open_atomic_invariant</a>

Macro used to temporarily “open” an
[`AtomicInvariant`](struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant")
object, obtaining the stored value within.

<a href="macro.open_atomic_invariant_in_proof.html" class="macro"
title="macro vstd::invariant::open_atomic_invariant_in_proof">open_atomic_invariant_in_proof</a>

<a href="macro.open_local_invariant.html" class="macro"
title="macro vstd::invariant::open_local_invariant">open_local_invariant</a>

Macro used to temporarily “open” a
[`LocalInvariant`](struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant")
object, obtaining the stored value within.

<a href="macro.open_local_invariant_in_proof.html" class="macro"
title="macro vstd::invariant::open_local_invariant_in_proof">open_local_invariant_in_proof</a>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.AtomicInvariant.html" class="struct"
title="struct vstd::invariant::AtomicInvariant">AtomicInvariant</a>  
An `AtomicInvariant` is a ghost object that provides “interior
mutability” for ghost objects, specifically, for `tracked` ghost
objects. A reference `&AtomicInvariant` may be shared between clients. A
client holding such a reference may *open* the invariant to obtain ghost
ownership of `v1: V`, and then *close* the invariant by returning ghost
ownership of a (potentially) different object `v2: V`.

<a href="struct.LocalInvariant.html" class="struct"
title="struct vstd::invariant::LocalInvariant">LocalInvariant</a>  
A `LocalInvariant` is a ghost object that provides “interior mutability”
for ghost objects, specifically, for `tracked` ghost objects. A
reference `&LocalInvariant` may be shared between clients. A client
holding such a reference may *open* the invariant to obtain ghost
ownership of `v1: V`, and then *close* the invariant by returning ghost
ownership of a (potentially) different object `v2: V`.

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>  
Trait used to specify an *invariant predicate* for
[`LocalInvariant`](struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant")
and
[`AtomicInvariant`](struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant").

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.create_open_invariant_credit.html" class="fn"
title="fn vstd::invariant::create_open_invariant_credit">create_open_invariant_credit</a>

</div>

</div>
