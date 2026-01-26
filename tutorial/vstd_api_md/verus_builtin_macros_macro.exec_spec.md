<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_builtin_macros](index.html)

</div>

# Macro <span class="macro">exec_spec</span> Copy item path

<span class="sub-heading"><a href="../src/verus_builtin_macros/lib.rs.html#452-454"
class="src">Source</a> </span>

</div>

``` rust
exec_spec!() { /* proc-macro */ }
```

Expand description

<div class="docblock">

Automatically compiles spec items to exec items, with proofs of
functional correctness.

This macro takes a list of spec items, and generates a corresponding
list of exec items:

- For every struct/enum `A`, we generate `ExecA`, which implements
  `DeepView<V = A>`
- For every spec function `spec fn f(T) -> U`, we generate
  <div class="example-wrap ignore">

  <a href="#" class="tooltip" title="This example is not tested">ⓘ</a>
  ``` rust
  fn exec_f(a: exec(T)) -> (r: exec(U))
  ensures r.deep_view() == f(a.deep_view()) { ... }
  ```

  </div>

  where `exec(T)` maps a subset of supported spec types to exec types,
  including `Seq` (translated to `Vec`) and `Option`.

Non-exhaustive list of supported spec expressions:

- Basic arithmetic operations
- Logical operators (&&, \|\|, &&&, \|\|\|, not, ==\>)
- If, match and “matches”
- Field expressions
- Two specific forms of quantifiers (`forall |x| ... <= x < ... ==> ...`
  and `exists |x| ... <= x < ... && ...`), which are compiled to loops.
- Spec function calls and recursion
- `Seq<T>` (compiled to `Vec<T>` or `&[T]` depending on the context),
  indexing, len, `seq!` literals
- `SpecString` (an alias to `Seq<char>` to syntactically indicate that
  we want `String`/`&str`), indexing, len, string literals
- `Option<T>`
- User-defined structs and enums
- Primitive integer/boolean types (`i<N>`, `isize`, `u<N>`, `usize`,
  `char`, etc.)
- Equality between Seq, String, and arithmetic types

</div>

</div>

</div>
