<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">assert_seqs_equal</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/seq_lib.rs.html#3649-3653" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! assert_seqs_equal {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Prove two sequences `s1` and `s2` are equal by proving that their
elements are equal at each index.

More precisely, `assert_seqs_equal!` requires:

- `s1` and `s2` have the same length (`s1.len() == s2.len()`), and
- for all `i` in the range `0 <= i < s1.len()`, we have
  `s1[i] == s2[i]`.

The property that equality follows from these facts is often called
*extensionality*.

`assert_seqs_equal!` can handle many trivial-looking identities without
any additional help:

<div class="example-wrap">

``` rust
proof fn subrange_concat(s: Seq<u64>, i: int) {
    requires([
        0 <= i && i <= s.len(),
    ]);

    let t1 = s.subrange(0, i);
    let t2 = s.subrange(i, s.len());
    let t = t1.add(t2);

    assert_seqs_equal!(s == t);

    assert(s == t);
}
```

</div>

In more complex cases, a proof may be required for the equality of each
element pair. For example,

<div class="example-wrap">

``` rust
proof fn bitvector_seqs() {
    let s = Seq::<u64>::new(5, |i| i as u64);
    let t = Seq::<u64>::new(5, |i| i as u64 | 0);

    assert_seqs_equal!(s == t, i => {
        // Need to show that s[i] == t[i]
        // Prove that the elements are equal by appealing to a bitvector solver:
        let j = i as u64;
        assert_bit_vector(j | 0 == j);
        assert(s[i] == t[i]);
    });
}
```

</div>

</div>

</div>

</div>
