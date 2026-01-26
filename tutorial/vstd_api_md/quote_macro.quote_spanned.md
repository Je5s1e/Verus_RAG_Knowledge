<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Macro <span class="macro">quote_spanned</span> Copy item path

<span class="sub-heading"><a href="../src/quote/lib.rs.html#631-635" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! quote_spanned {
    ($span:expr=> $($tt:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

Same as `quote!`, but applies a given span to all tokens originating
within the macro invocation.

  

## <a href="#syntax" class="doc-anchor">§</a>Syntax

A span expression of type
[`Span`](../proc_macro2/struct.Span.html "struct proc_macro2::Span"),
followed by `=>`, followed by the tokens to quote. The span expression
should be brief — use a variable for anything more than a few
characters. There should be no space before the `=>` token.

<div class="example-wrap">

``` rust
let span = /* ... */;

// On one line, use parentheses.
let tokens = quote_spanned!(span=> Box::into_raw(Box::new(#init)));

// On multiple lines, place the span at the top and use braces.
let tokens = quote_spanned! {span=>
    Box::into_raw(Box::new(#init))
};
```

</div>

The lack of space before the `=>` should look jarring to Rust
programmers and this is intentional. The formatting is designed to be
visibly off-balance and draw the eye a particular way, due to the span
expression being evaluated in the context of the procedural macro and
the remaining tokens being evaluated in the generated code.

  

## <a href="#hygiene" class="doc-anchor">§</a>Hygiene

Any interpolated tokens preserve the `Span` information provided by
their `ToTokens` implementation. Tokens that originate within the
`quote_spanned!` invocation are spanned with the given span argument.

  

## <a href="#example" class="doc-anchor">§</a>Example

The following procedural macro code uses `quote_spanned!` to assert that
a particular Rust type implements the
[`Sync`](https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html "trait core::marker::Sync")
trait so that references can be safely shared between threads.

<div class="example-wrap">

``` rust
let ty_span = ty.span();
let assert_sync = quote_spanned! {ty_span=>
    struct _AssertSync where #ty: Sync;
};
```

</div>

If the assertion fails, the user will see an error like the following.
The input span of their type is highlighted in the error.

<div class="example-wrap">

``` text
error[E0277]: the trait bound `*const (): std::marker::Sync` is not satisfied
  --> src/main.rs:10:21
   |
10 |     static ref PTR: *const () = &();
   |                     ^^^^^^^^^ `*const ()` cannot be shared between threads safely
```

</div>

In this example it is important for the where-clause to be spanned with
the line/column information of the user’s input type so that error
messages are placed appropriately by the compiler.

</div>

</div>

</div>
