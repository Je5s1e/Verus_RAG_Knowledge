<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[invariant](index.html)

</div>

# Macro <span class="macro">open_atomic_invariant</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/invariant.rs.html#398-406"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! open_atomic_invariant {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Macro used to temporarily “open” an
[`AtomicInvariant`](struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant")
object, obtaining the stored value within.

#### <a href="#usage" class="doc-anchor">§</a>Usage

The form of the macro looks like,

<div class="example-wrap">

``` rust
open_atomic_invariant($inv => $id => {
    // Inner scope
});
```

</div>

This operation is very similar to
[`open_local_invariant!`](../macro.open_local_invariant.html "macro vstd::open_local_invariant"),
so we refer to its documentation for the basics. There is only one
difference, besides the fact that `$inv` should be an
[`&AtomicInvariant`](struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant")
rather than a
[`&LocalInvariant`](struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant").
The difference is that `open_atomic_invariant!` has an additional
*atomicity constraint*:

- **Atomicity constraint**: The code body of an `open_atomic_invariant!`
  block cannot contain any `exec`-mode code with the exception of a
  *single* atomic operation.

(Of course, the code block can still contain an arbitrary amount of
ghost code.)

The atomicity constraint is needed because an `AtomicInvariant` must be
thread-safe; that is, it can be shared across threads. In order for the
ghost state to be shared safely, it must be restored after each atomic
operation.

The atomic operations may be found in the
[`PAtomic`](../atomic/index.html "mod vstd::atomic") library. The user
can also mark their own functions as “atomic operations” using
`#[verifier::atomic)]`; however, this is not useful for very much other
than defining wrappers around the existing atomic operations from
[`PAtomic`](../atomic/index.html "mod vstd::atomic"). Note that reading
and writing through a
[`PCell`](../cell/struct.PCell.html "struct vstd::cell::PCell") or a
[`PPtr`](../simple_pptr/struct.PPtr.html "struct vstd::simple_pptr::PPtr")
are *not* atomic operations.

**Note:** Rather than using `open_atomic_invariant!` directly, we
generally recommend using the [`atomic_ghost`
APIs](../atomic_ghost/index.html "mod vstd::atomic_ghost").

It’s not legal to use `open_atomic_invariant!` in proof mode. In proof
mode, you need to use `open_atomic_invariant_in_proof!` instead. This
takes one extra parameter, an open-invariant credit, which you can get
by calling `create_open_invariant_credit()` before you enter proof mode.

#### <a href="#example" class="doc-anchor">§</a>Example

TODO fill this in

</div>

</div>

</div>
