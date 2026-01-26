<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate vstd Copy item path

<span class="sub-heading"><a href="../src/vstd/vstd.rs.html#1-138" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

The “standard library” for [Verus](https://github.com/verus-lang/verus).
Contains various utilities and datatypes for proofs, as well as runtime
functionality with specifications. For an introduction to Verus, see
[the tutorial](https://verus-lang.github.io/verus/guide/).

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="arithmetic/index.html" class="mod"
title="mod vstd::arithmetic">arithmetic</a>

<a href="array/index.html" class="mod" title="mod vstd::array">array</a>

<a href="atomic/index.html" class="mod"
title="mod vstd::atomic">atomic</a>

<a href="atomic_ghost/index.html" class="mod"
title="mod vstd::atomic_ghost">atomic_ghost</a>

Provides sequentially-consistent atomic memory locations with associated
ghost state. See the
[`atomic_with_ghost!`](macro.atomic_with_ghost.html "macro vstd::atomic_with_ghost")
documentation for more information.

<a href="bits/index.html" class="mod" title="mod vstd::bits">bits</a>

Properties of bitwise operators.

<a href="bytes/index.html" class="mod" title="mod vstd::bytes">bytes</a>

Conversions to/from bytes

<a href="calc_macro/index.html" class="mod"
title="mod vstd::calc_macro">calc_macro</a>

The [`calc`](macro.calc.html "macro vstd::calc") macro provides support
for reasoning about a structured proof calculation.

<a href="cell/index.html" class="mod" title="mod vstd::cell">cell</a>

<a href="compute/index.html" class="mod"
title="mod vstd::compute">compute</a>

<a href="contrib/index.html" class="mod"
title="mod vstd::contrib">contrib</a>

<a href="float/index.html" class="mod" title="mod vstd::float">float</a>

Properties of floating point values.

<a href="function/index.html" class="mod"
title="mod vstd::function">function</a>

<a href="hash_map/index.html" class="mod"
title="mod vstd::hash_map">hash_map</a>

<a href="hash_set/index.html" class="mod"
title="mod vstd::hash_set">hash_set</a>

<a href="invariant/index.html" class="mod"
title="mod vstd::invariant">invariant</a>

<a href="layout/index.html" class="mod"
title="mod vstd::layout">layout</a>

<a href="logatom/index.html" class="mod"
title="mod vstd::logatom">logatom</a>

<a href="map/index.html" class="mod" title="mod vstd::map">map</a>

<a href="map_lib/index.html" class="mod"
title="mod vstd::map_lib">map_lib</a>

<a href="math/index.html" class="mod" title="mod vstd::math">math</a>

<a href="modes/index.html" class="mod" title="mod vstd::modes">modes</a>

<a href="multiset/index.html" class="mod"
title="mod vstd::multiset">multiset</a>

<a href="multiset_lib/index.html" class="mod"
title="mod vstd::multiset_lib">multiset_lib</a>

<a href="pcm/index.html" class="mod" title="mod vstd::pcm">pcm</a>

<a href="pcm_lib/index.html" class="mod"
title="mod vstd::pcm_lib">pcm_lib</a>

<a href="pervasive/index.html" class="mod"
title="mod vstd::pervasive">pervasive</a>

<a href="prelude/index.html" class="mod"
title="mod vstd::prelude">prelude</a>

<a href="proph/index.html" class="mod" title="mod vstd::proph">proph</a>

<a href="raw_ptr/index.html" class="mod"
title="mod vstd::raw_ptr">raw_ptr</a>

Tools and reasoning principles for [raw
pointers](https://doc.rust-lang.org/std/primitive.pointer.html). The
tools here are meant to address “real Rust pointers, including all their
subtleties on the Rust Abstract Machine, to the largest extent that is
reasonable.”

<a href="relations/index.html" class="mod"
title="mod vstd::relations">relations</a>

Provides specifications for spec closures as relations.

<a href="rwlock/index.html" class="mod"
title="mod vstd::rwlock">rwlock</a>

<a href="seq/index.html" class="mod" title="mod vstd::seq">seq</a>

<a href="seq_lib/index.html" class="mod"
title="mod vstd::seq_lib">seq_lib</a>

<a href="set/index.html" class="mod" title="mod vstd::set">set</a>

<a href="set_lib/index.html" class="mod"
title="mod vstd::set_lib">set_lib</a>

<a href="shared/index.html" class="mod"
title="mod vstd::shared">shared</a>

<a href="simple_pptr/index.html" class="mod"
title="mod vstd::simple_pptr">simple_pptr</a>

<a href="slice/index.html" class="mod" title="mod vstd::slice">slice</a>

<a href="storage_protocol/index.html" class="mod"
title="mod vstd::storage_protocol">storage_protocol</a>

<a href="string/index.html" class="mod"
title="mod vstd::string">string</a>

<a href="thread/index.html" class="mod"
title="mod vstd::thread">thread</a>

<a href="tokens/index.html" class="mod"
title="mod vstd::tokens">tokens</a>

<a href="view/index.html" class="mod" title="mod vstd::view">view</a>

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.assert_by_contradiction.html" class="macro"
title="macro vstd::assert_by_contradiction">assert_by_contradiction</a>  
Allows you to prove a boolean predicate by assuming its negation and
proving a contradiction.

<a href="macro.assert_maps_equal.html" class="macro"
title="macro vstd::assert_maps_equal">assert_maps_equal</a>  
Prove two maps `map1` and `map2` are equal by proving that their values
are equal at each key.

<a href="macro.assert_multisets_equal.html" class="macro"
title="macro vstd::assert_multisets_equal">assert_multisets_equal</a>  
<a href="macro.assert_multisets_equal_internal.html" class="macro"
title="macro vstd::assert_multisets_equal_internal">assert_multisets_equal_internal</a>  
<a href="macro.assert_seqs_equal.html" class="macro"
title="macro vstd::assert_seqs_equal">assert_seqs_equal</a>  
Prove two sequences `s1` and `s2` are equal by proving that their
elements are equal at each index.

<a href="macro.assert_sets_equal.html" class="macro"
title="macro vstd::assert_sets_equal">assert_sets_equal</a>  
Prove two sets equal by extensionality. Usage is:

<a href="macro.atomic_with_ghost.html" class="macro"
title="macro vstd::atomic_with_ghost">atomic_with_ghost</a>  
Performs a given atomic operation on a given atomic while providing
access to its ghost state.

<a href="macro.calc.html" class="macro"
title="macro vstd::calc">calc</a>  
The `calc!` macro supports structured proofs through calculations.

<a href="macro.map.html" class="macro" title="macro vstd::map">map</a>  
Create a map using syntax like `map![key1 => val1, key2 => val, ...]`.

<a href="macro.open_atomic_invariant.html" class="macro"
title="macro vstd::open_atomic_invariant">open_atomic_invariant</a>  
Macro used to temporarily “open” an
[`AtomicInvariant`](invariant/struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant")
object, obtaining the stored value within.

<a href="macro.open_atomic_invariant_in_proof.html" class="macro"
title="macro vstd::open_atomic_invariant_in_proof">open_atomic_invariant_in_proof</a>  
<a href="macro.open_atomic_invariant_in_proof_internal.html"
class="macro"
title="macro vstd::open_atomic_invariant_in_proof_internal">open_atomic_invariant_in_proof_internal</a>  
<a href="macro.open_atomic_invariant_internal.html" class="macro"
title="macro vstd::open_atomic_invariant_internal">open_atomic_invariant_internal</a>  
<a href="macro.open_local_invariant.html" class="macro"
title="macro vstd::open_local_invariant">open_local_invariant</a>  
Macro used to temporarily “open” a
[`LocalInvariant`](invariant/struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant")
object, obtaining the stored value within.

<a href="macro.open_local_invariant_in_proof.html" class="macro"
title="macro vstd::open_local_invariant_in_proof">open_local_invariant_in_proof</a>  
<a href="macro.open_local_invariant_in_proof_internal.html"
class="macro"
title="macro vstd::open_local_invariant_in_proof_internal">open_local_invariant_in_proof_internal</a>  
<a href="macro.open_local_invariant_internal.html" class="macro"
title="macro vstd::open_local_invariant_internal">open_local_invariant_internal</a>  
<a href="macro.pcell_points.html" class="macro"
title="macro vstd::pcell_points">pcell_points</a>  
<a href="macro.seq.html" class="macro" title="macro vstd::seq">seq</a>  
Creates a [`Seq`](seq/struct.Seq.html "struct vstd::seq::Seq")
containing the given elements.

<a href="macro.set.html" class="macro" title="macro vstd::set">set</a>  
<a href="macro.vpanic.html" class="macro"
title="macro vstd::vpanic">vpanic</a>  
Replace panic macro with vpanic when needed. panic!{} may call panic_fmt
with private rt::Argument, which could not be supported in verus.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.group_vstd_default.html" class="fn"
title="fn vstd::group_vstd_default">group_vstd_default</a>

</div>

</div>
