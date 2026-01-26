<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">assert_maps_equal</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/map.rs.html#390-394" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! assert_maps_equal {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Prove two maps `map1` and `map2` are equal by proving that their values
are equal at each key.

More precisely, `assert_maps_equal!` requires that for each key `k`:

- `map1` contains `k` in its domain if and only if `map2` does
  (`map1.dom().contains(k) <==> map2.dom().contains(k)`)
- If they contain `k` in their domains, then their values are equal
  (`map1.dom().contains(k) && map2.dom().contains(k) ==> map1[k] == map2[k]`)

The property that equality follows from these facts is often called
*extensionality*.

`assert_maps_equal!` can handle many trivial-looking identities without
any additional help:

<div class="example-wrap">

``` rust
proof fn insert_remove(m: Map<int, int>, k: int, v: int)
    requires !m.dom().contains(k)
    ensures m.insert(k, v).remove(k) == m
{
    let m2 = m.insert(k, v).remove(k);
    assert_maps_equal!(m == m2);
    assert(m == m2);
}
```

</div>

For more complex cases, a proof may be required for each key:

<div class="example-wrap">

``` rust
proof fn bitvector_maps() {
    let m1 = Map::<u64, u64>::new(
        |key: u64| key & 31 == key,
        |key: u64| key | 5);

    let m2 = Map::<u64, u64>::new(
        |key: u64| key < 32,
        |key: u64| 5 | key);

    assert_maps_equal!(m1 == m2, key => {
        // Show that the domains of m1 and m2 are the same by showing their predicates
        // are equivalent.
        assert_bit_vector((key & 31 == key) <==> (key < 32));

        // Show that the values are the same by showing that these expressions
        // are equivalent.
        assert_bit_vector(key | 5 == 5 | key);
    });
}
```

</div>

</div>

</div>

</div>
