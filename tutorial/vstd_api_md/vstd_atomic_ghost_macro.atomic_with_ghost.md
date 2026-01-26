<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[atomic_ghost](index.html)

</div>

# Macro <span class="macro">atomic_with_ghost</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/atomic_ghost.rs.html#326-334"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! atomic_with_ghost {
    ($($tokens:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

Performs a given atomic operation on a given atomic while providing
access to its ghost state.

`atomic_with_ghost!` supports the types
[`AtomicU64`](struct.AtomicU64.html "struct vstd::atomic_ghost::AtomicU64")
[`AtomicU32`](struct.AtomicU32.html "struct vstd::atomic_ghost::AtomicU32"),
[`AtomicU16`](struct.AtomicU16.html "struct vstd::atomic_ghost::AtomicU16"),
[`AtomicU8`](struct.AtomicU8.html "struct vstd::atomic_ghost::AtomicU8"),
[`AtomicI64`](struct.AtomicI64.html "struct vstd::atomic_ghost::AtomicI64"),
[`AtomicI32`](struct.AtomicI32.html "struct vstd::atomic_ghost::AtomicI32"),
[`AtomicI16`](struct.AtomicI16.html "struct vstd::atomic_ghost::AtomicI16"),
[`AtomicI8`](struct.AtomicI8.html "struct vstd::atomic_ghost::AtomicI8"),
and
[`AtomicBool`](struct.AtomicBool.html "struct vstd::atomic_ghost::AtomicBool").

For each type, it supports all applicable atomic operations among
`load`, `store`, `swap`, `compare_exchange`, `compare_exchange_weak`,
`fetch_add`, `fetch_add_wrapping`, `fetch_sub`, `fetch_sub_wrapping`,
`fetch_or`, `fetch_and`, `fetch_xor`, `fetch_nand`, `fetch_max`, and
`fetch_min`.

Naturally, `AtomicBool` does not support the arithmetic-specific
operations.

In general, the syntax is:

<div class="example-wrap">

``` rust
let result = atomic_with_ghost!(
    $atomic => $operation_name($operands...);
    update $prev -> $next;         // `update` line is optional
    returning $ret;                // `returning` line is optional
    ghost $g => {
        /* Proof code with access to `tracked` variable `g: G` */
    }
);
```

</div>

Here, the `$operation_name` is one of `load`, `store`, etc. Meanwhile,
`$prev`, `$next`, and `$ret` are all identifiers which will be available
as spec variable inside the block to describe the atomic action which is
performed.

For example, suppose the user performs `fetch_add(1)`. The atomic
operation might load the value 5, add 1, store the value 6, and return
the original value, 5. In that case, we would have `prev == 5`,
`next == 6`, and `ret == 5`.

The specification for a given operation is given as a relation between
`prev`, `next`, and `ret`; that is, at the beginning of the proof block,
the user may assume the given specification holds:

<div>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>operation</th>
<th>specification</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>load()</code></td>
<td><code>next == prev &amp;&amp; rev == prev</code></td>
</tr>
<tr>
<td><code>store(x)</code></td>
<td><code>next == x &amp;&amp; ret == ()</code></td>
</tr>
<tr>
<td><code>swap(x)</code></td>
<td><code>next == x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>compare_exchange(x, y)</code></td>
<td><code>prev == x &amp;&amp; next == y &amp;&amp; ret == Ok(prev)</code>
(“success”) OR<br />
<code>prev != x &amp;&amp; next == prev &amp;&amp; ret == Err(prev)</code>
(“failure”)</td>
</tr>
<tr>
<td><code>compare_exchange_weak(x, y)</code></td>
<td><code>prev == x &amp;&amp; next == y &amp;&amp; ret == Ok(prev)</code>
(“success”) OR<br />
<code>next == prev &amp;&amp; ret == Err(prev)</code> (“failure”)</td>
</tr>
<tr>
<td><code>fetch_add(x)</code> (*)</td>
<td><code>next == prev + x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_add_wrapping(x)</code></td>
<td><code>next == wrapping_add(prev, x) &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_sub(x)</code> (*)</td>
<td><code>next == prev - x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_sub_wrapping(x)</code></td>
<td><code>next == wrapping_sub(prev, x) &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_or(x)</code></td>
<td><code>next == prev | x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_and(x)</code></td>
<td><code>next == prev &amp; x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_xor(x)</code></td>
<td><code>next == prev ^ x &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_nand(x)</code></td>
<td><code>next == !(prev &amp; x) &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_max(x)</code></td>
<td><code>next == max(prev, x) &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>fetch_min(x)</code></td>
<td><code>next == max(prev, x) &amp;&amp; ret == prev</code></td>
</tr>
<tr>
<td><code>no_op()</code> (**)</td>
<td><code>next == prev &amp;&amp; ret == ()</code></td>
</tr>
</tbody>
</table>

</div>

(\*) Note that `fetch_add` and `fetch_sub` do not specify
wrapping-on-overflow; instead, they require the user to prove that
overflow *does not occur*, i.e., the user must show that `next` is in
bounds for the integer type in question. Furthermore, for `fetch_add`
and `fetch_sub`, the spec values of `prev`, `next`, and `ret` are all
given with type `int`, so the user may reason about boundedness within
the proof block.

(As executable code, `fetch_add` is equivalent to `fetch_add_wrapping`,
and likewise for `fetch_sub` and `fetch_sub_wrapping`. We have both
because it’s frequently the case that the user needs to verify
lack-of-overflow *anyway*, and having it as an explicit precondition by
default then makes verification errors easier to diagnose. Furthermore,
when overflow is intended, the wrapping operations document that
intent.)

(\*\*) `no_op` is entirely a ghost operation and doesn’t emit any actual
instruction. This allows the user to access the ghost state and the
stored value (as `spec` data) without actually performing a load.

------------------------------------------------------------------------

At the beginning of the proof block, the user may assume, in addition to
the specified relation between `prev`, `next`, and `ret`, that
`atomic.inv(prev, g)` holds. The user is required to update `g` such
that `atomic.inv(next, g)` holds at the end of the block. In other
words, the ghost block has the implicit pre- and post-conditions:

<div class="example-wrap">

``` rust
let result = atomic_with_ghost!(
    $atomic => $operation_name($operands...);
    update $prev -> $next;
    returning $ret;
    ghost $g => {
        assume(specified relation on (prev, next, ret));
        assume(atomic.inv(prev, g));

        // User code here; may update variable `g` with full
        // access to variables in the outer context.

        assert(atomic.inv(next, g));
    }
);
```

</div>

Note that the necessary action on ghost state might depend on the result
of the operation; for example, if the user performs a compare-and-swap,
then the ghost action that they then need to do will probably depend on
whether the operation succeeded or not.

The value returned by the `atomic_with_ghost!(...)` expression will be
equal to `ret`, although the return value is an `exec` value (the actual
result of the operation) while `ret` is a `spec` value.

#### <a href="#example-todo" class="doc-anchor">§</a>Example (TODO)

</div>

</div>

</div>
