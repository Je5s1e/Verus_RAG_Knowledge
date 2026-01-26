<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[invariant](index.html)

</div>

# Macro <span class="macro">open_local_invariant</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/invariant.rs.html#548-555"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! open_local_invariant {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Macro used to temporarily “open” a
[`LocalInvariant`](struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant")
object, obtaining the stored value within.

#### <a href="#usage" class="doc-anchor">§</a>Usage

The form of the macro looks like,

<div class="example-wrap">

``` rust
open_local_invariant($inv => $id => {
    // Inner scope
});
```

</div>

The operation of opening an invariant is a ghost one; however, the inner
code block may contain arbitrary `exec`-mode code. The invariant remains
“open” for the duration of the inner code block, and it is closed again
of the end of the block.

The `$inv` parameter should be an expression of type
`&LocalInvariant<K, V, Pred>`, the invariant object to be opened. The
`$id` is an identifier which is bound within the code block as a `mut`
variable of type `V`. This gives the user ownership over the `V` value,
which they may manipulate freely within the code block. At the end of
the code block, the variable `$id` is consumed.

The obtained object `v: V`, will satisfy the `LocalInvariant`’s
invariant predicate [`$inv.inv(v)`](LocalInvariant::inv). Furthermore,
the user must prove that this invariant still holds at the end. In other
words, the macro usage is roughly equivalent to the following:

<div class="example-wrap">

``` rust
{
    let $id: V = /* an arbitrary value */;
    assume($inv.inv($id));
    /* user code block here */
    assert($inv.inv($id));
    consume($id);
}
```

</div>

#### <a href="#avoiding-reentrancy" class="doc-anchor">§</a>Avoiding Reentrancy

Verus adds additional checks to ensure that an invariant is never opened
more than once at the same time. For example, suppose that you attempt
to nest the use of `open_invariant`, supplying the same argument `inv`
to each:

<div class="example-wrap">

``` rust
open_local_invariant(inv => id1 => {
    open_local_invariant(inv => id2 => {
    });
});
```

</div>

In this situation, Verus would produce an error:

<div class="example-wrap">

``` rust
error: possible invariant collision
  |
  |   open_local_invariant!(&inv => id1 => {
  |                           ^ this invariant
  |       open_local_invariant!(&inv => id2 => {
  |                               ^ might be the same as this invariant
  ...
  |       }
  |   }
```

</div>

When generating these conditions, Verus compares invariants via their
[`namespace()`](LocalInvariant::namespace) values. An invariant’s
namespace (represented simply as an integer) is specified upon the call
to \[`LocalInvariant::new`\]. If you have the need to open multiple
invariants at once, make sure to given them different namespaces.

So that Verus can ensure that there are no nested invariant accesses
across function boundaries, every `proof` and `exec` function has, as
part of its specification, the set of invariant namespaces that it might
open.

The invariant set of a function can be specified via the
[`opens_invariants`
clause](https://verus-lang.github.io/verus/guide/reference-opens-invariants.html).
The default for an `exec`-mode function is to open any, while the
default for a `proof`-mode function is to open none.

It’s not legal to use `open_local_invariant!` in proof mode. In proof
mode, you need to use `open_local_invariant_in_proof!` instead. This
takes one extra parameter, an open-invariant credit, which you can get
by calling `create_open_invariant_credit()` before you enter proof mode.

#### <a href="#example" class="doc-anchor">§</a>Example

TODO fill this in

#### <a href="#more-examples" class="doc-anchor">§</a>More Examples

TODO fill this in

</div>

</div>

</div>
