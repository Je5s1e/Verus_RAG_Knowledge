<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate verus_syn Copy item path

<span class="sub-heading"><a href="../src/verus_syn/lib.rs.html#1-1146" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

[![github](https://img.shields.io/badge/github-8da0cb?style=for-the-badge&labelColor=555555&logo=github)](https://github.com/dtolnay/syn) [![crates-io](https://img.shields.io/badge/crates.io-fc8d62?style=for-the-badge&labelColor=555555&logo=rust)](https://crates.io/crates/syn) [![docs-rs](https://img.shields.io/badge/docs.rs-66c2a5?style=for-the-badge&labelColor=555555&logo=docs.rs)](index.html "mod verus_syn")

  

Syn is a parsing library for parsing a stream of Rust tokens into a
syntax tree of Rust source code.

Currently this library is geared toward use in Rust procedural macros,
but contains some APIs that may be useful more generally.

- **Data structures** — Syn provides a complete syntax tree that can
  represent any valid Rust source code. The syntax tree is rooted at
  [`syn::File`](struct.File.html "struct verus_syn::File") which
  represents a full source file, but there are other entry points that
  may be useful to procedural macros including
  [`syn::Item`](enum.Item.html "enum verus_syn::Item"),
  [`syn::Expr`](enum.Expr.html "enum verus_syn::Expr") and
  [`syn::Type`](enum.Type.html "enum verus_syn::Type").

- **Derives** — Of particular interest to derive macros is
  [`syn::DeriveInput`](struct.DeriveInput.html "struct verus_syn::DeriveInput")
  which is any of the three legal input items to a derive macro. An
  example below shows using this type in a library that can derive
  implementations of a user-defined trait.

- **Parsing** — Parsing in Syn is built around [parser
  functions](parse/index.html "mod verus_syn::parse") with the signature
  `fn(ParseStream) -> Result<T>`. Every syntax tree node defined by Syn
  is individually parsable and may be used as a building block for
  custom syntaxes, or you may dream up your own brand new syntax without
  involving any of our syntax tree types.

- **Location information** — Every token parsed by Syn is associated
  with a `Span` that tracks line and column information back to the
  source of that token. These spans allow a procedural macro to display
  detailed error messages pointing to all the right places in the user’s
  code. There is an example of this below.

- **Feature flags** — Functionality is aggressively feature gated so
  your procedural macros enable only what they need, and do not pay in
  compile time for all the rest.

  

## <a href="#example-of-a-derive-macro" class="doc-anchor">§</a>Example of a derive macro

The canonical derive macro using Syn looks like this. We write an
ordinary Rust function tagged with a `proc_macro_derive` attribute and
the name of the trait we are deriving. Any time that derive appears in
the user’s code, the Rust compiler passes their data structure as tokens
into our macro. We get to execute arbitrary Rust code to figure out what
to do with those tokens, then hand some tokens back to the compiler to
compile into the user’s crate.

<div class="example-wrap">

``` toml
[dependencies]
syn = "2.0"
quote = "1.0"

[lib]
proc-macro = true
```

</div>

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(MyMacro)]
pub fn my_macro(input: TokenStream) -> TokenStream {
    // Parse the input tokens into a syntax tree
    let input = parse_macro_input!(input as DeriveInput);

    // Build the output, possibly using quasi-quotation
    let expanded = quote! {
        // ...
    };

    // Hand the output tokens back to the compiler
    TokenStream::from(expanded)
}
```

</div>

The
[`heapsize`](https://github.com/dtolnay/syn/tree/master/examples/heapsize)
example directory shows a complete working implementation of a derive
macro. The example derives a `HeapSize` trait which computes an estimate
of the amount of heap memory owned by a value.

<div class="example-wrap">

``` rust
pub trait HeapSize {
    /// Total number of bytes of heap memory owned by `self`.
    fn heap_size_of_children(&self) -> usize;
}
```

</div>

The derive macro allows users to write `#[derive(HeapSize)]` on data
structures in their program.

<div class="example-wrap">

``` rust
#[derive(HeapSize)]
struct Demo<'a, T: ?Sized> {
    a: Box<T>,
    b: u8,
    c: &'a str,
    d: String,
}
```

</div>

  

## <a href="#spans-and-error-reporting" class="doc-anchor">§</a>Spans and error reporting

The token-based procedural macro API provides great control over where
the compiler’s error messages are displayed in user code. Consider the
error the user sees if one of their field types does not implement
`HeapSize`.

<div class="example-wrap">

``` rust
#[derive(HeapSize)]
struct Broken {
    ok: String,
    bad: std::thread::Thread,
}
```

</div>

By tracking span information all the way through the expansion of a
procedural macro as shown in the `heapsize` example, token-based macros
in Syn are able to trigger errors that directly pinpoint the source of
the problem.

<div class="example-wrap">

``` text
error[E0277]: the trait bound `std::thread::Thread: HeapSize` is not satisfied
 --> src/main.rs:7:5
  |
7 |     bad: std::thread::Thread,
  |     ^^^^^^^^^^^^^^^^^^^^^^^^ the trait `HeapSize` is not implemented for `Thread`
```

</div>

  

## <a href="#parsing-a-custom-syntax" class="doc-anchor">§</a>Parsing a custom syntax

The
[`lazy-static`](https://github.com/dtolnay/syn/tree/master/examples/lazy-static)
example directory shows the implementation of a `functionlike!(...)`
procedural macro in which the input tokens are parsed using Syn’s
parsing API.

The example reimplements the popular `lazy_static` crate from crates.io
as a procedural macro.

<div class="example-wrap">

``` rust
lazy_static! {
    static ref USERNAME: Regex = Regex::new("^[a-z0-9_-]{3,16}$").unwrap();
}
```

</div>

The implementation shows how to trigger custom warnings and error
messages on the macro input.

<div class="example-wrap">

``` text
warning: come on, pick a more creative name
  --> src/main.rs:10:16
   |
10 |     static ref FOO: String = "lazy_static".to_owned();
   |                ^^^
```

</div>

  

## <a href="#testing" class="doc-anchor">§</a>Testing

When testing macros, we often care not just that the macro can be used
successfully but also that when the macro is provided with invalid input
it produces maximally helpful error messages. Consider using the
[`trybuild`](https://github.com/dtolnay/trybuild) crate to write tests
for errors that are emitted by your macro or errors detected by the Rust
compiler in the expanded code following misuse of the macro. Such tests
help avoid regressions from later refactors that mistakenly make an
error no longer trigger or be less helpful than it used to be.

  

## <a href="#debugging" class="doc-anchor">§</a>Debugging

When developing a procedural macro it can be helpful to look at what the
generated code looks like. Use
`cargo rustc -- -Zunstable-options --pretty=expanded` or the
[`cargo expand`](https://github.com/dtolnay/cargo-expand) subcommand.

To show the expanded code for some crate that uses your procedural
macro, run `cargo expand` from that crate. To show the expanded code for
one of your own test cases, run `cargo expand --test the_test_case`
where the last argument is the name of the test file without the `.rs`
extension.

This write-up by Brandon W Maister discusses debugging in more detail:
[Debugging Rust’s new Custom Derive
system](https://quodlibetor.github.io/posts/debugging-rusts-new-custom-derive-system/).

  

## <a href="#optional-features" class="doc-anchor">§</a>Optional features

Syn puts a lot of functionality behind optional features in order to
optimize compile time for the most common use cases. The following
features are available.

- **`derive`** *(enabled by default)* — Data structures for representing
  the possible input to a derive macro, including structs and enums and
  types.
- **`full`** — Data structures for representing the syntax tree of all
  valid Rust source code, including items and expressions.
- **`parsing`** *(enabled by default)* — Ability to parse input tokens
  into a syntax tree node of a chosen type.
- **`printing`** *(enabled by default)* — Ability to print a syntax tree
  node as tokens of Rust source code.
- **`visit`** — Trait for traversing a syntax tree.
- **`visit-mut`** — Trait for traversing and mutating in place a syntax
  tree.
- **`fold`** — Trait for transforming an owned syntax tree.
- **`clone-impls`** *(enabled by default)* — Clone impls for all syntax
  tree types.
- **`extra-traits`** — Debug, Eq, PartialEq, Hash impls for all syntax
  tree types.
- **`proc-macro`** *(enabled by default)* — Runtime dependency on the
  dynamic library libproc_macro from rustc toolchain.

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="buffer/index.html" class="mod"
title="mod verus_syn::buffer">buffer</a>  
A stably addressed token buffer supporting efficient traversal based on
a cheaply copyable cursor.

<a href="ext/index.html" class="mod" title="mod verus_syn::ext">ext</a>  
Extension traits to provide parsing methods on foreign types.

<a href="meta/index.html" class="mod"
title="mod verus_syn::meta">meta</a>  
Facility for interpreting structured content inside of an `Attribute`.

<a href="parse/index.html" class="mod"
title="mod verus_syn::parse">parse</a>  
Parsing interface for parsing a token stream into a syntax tree node.

<a href="punctuated/index.html" class="mod"
title="mod verus_syn::punctuated">punctuated</a>  
A punctuated sequence of syntax tree nodes separated by punctuation.

<a href="spanned/index.html" class="mod"
title="mod verus_syn::spanned">spanned</a>  
A trait that can provide the `Span` of the complete contents of a syntax
tree node.

<a href="token/index.html" class="mod"
title="mod verus_syn::token">token</a>  
Tokens representing Rust punctuation, keywords, and delimiters.

<a href="visit/index.html" class="mod"
title="mod verus_syn::visit">visit</a>  
Syntax tree traversal to walk a shared borrow of a syntax tree.

<a href="visit_mut/index.html" class="mod"
title="mod verus_syn::visit_mut">visit_mut</a>  
Syntax tree traversal to mutate an exclusive borrow of a syntax tree in
place.

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.Token.html" class="macro"
title="macro verus_syn::Token">Token</a>  
A type-macro that expands to the name of the Rust type representation of
a given token.

<a href="macro.braced.html" class="macro"
title="macro verus_syn::braced">braced</a>  
Parse a set of curly braces and expose their content to subsequent
parsers.

<a href="macro.bracketed.html" class="macro"
title="macro verus_syn::bracketed">bracketed</a>  
Parse a set of square brackets and expose their content to subsequent
parsers.

<a href="macro.custom_keyword.html" class="macro"
title="macro verus_syn::custom_keyword">custom_keyword</a>  
Define a type that supports parsing and printing a given identifier as
if it were a keyword.

<a href="macro.custom_punctuation.html" class="macro"
title="macro verus_syn::custom_punctuation">custom_punctuation</a>  
Define a type that supports parsing and printing a multi-character
symbol as if it were a punctuation token.

<a href="macro.parenthesized.html" class="macro"
title="macro verus_syn::parenthesized">parenthesized</a>  
Parse a set of parentheses and expose their content to subsequent
parsers.

<a href="macro.parse_macro_input.html" class="macro"
title="macro verus_syn::parse_macro_input">parse_macro_input</a>  
Parse the input TokenStream of a macro, triggering a compile error if
the tokens fail to parse.

<a href="macro.parse_quote.html" class="macro"
title="macro verus_syn::parse_quote">parse_quote</a>  
Quasi-quotation macro that accepts input like the
[`quote!`](https://docs.rs/quote/1.0/quote/index.html) macro but uses
type inference to figure out a return type for those tokens.

<a href="macro.parse_quote_spanned.html" class="macro"
title="macro verus_syn::parse_quote_spanned">parse_quote_spanned</a>  
This macro is
[`parse_quote!`](macro.parse_quote.html "macro verus_syn::parse_quote") +
[`quote_spanned!`](../quote/macro.quote_spanned.html "macro quote::quote_spanned").

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Abi.html" class="struct"
title="struct verus_syn::Abi">Abi</a>

The binary interface of a function: `extern "C"`.

<a href="struct.AngleBracketedGenericArguments.html" class="struct"
title="struct verus_syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>

Angle bracketed arguments of a path segment: the `<K, V>` in
`HashMap<K, V>`.

<a href="struct.Arm.html" class="struct"
title="struct verus_syn::Arm">Arm</a>

One arm of a `match` expression: `0..=10 => { return true; }`.

<a href="struct.Assert.html" class="struct"
title="struct verus_syn::Assert">Assert</a>

<a href="struct.AssertForall.html" class="struct"
title="struct verus_syn::AssertForall">AssertForall</a>

<a href="struct.AssocConst.html" class="struct"
title="struct verus_syn::AssocConst">AssocConst</a>

An equality constraint on an associated constant: the `PANIC = false` in
`Trait<PANIC = false>`.

<a href="struct.AssocType.html" class="struct"
title="struct verus_syn::AssocType">AssocType</a>

A binding (equality constraint) on an associated type: the `Item = u8`
in `Iterator<Item = u8>`.

<a href="struct.Assume.html" class="struct"
title="struct verus_syn::Assume">Assume</a>

<a href="struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::AssumeSpecification">AssumeSpecification</a>

<a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

An attribute, like `#[repr(transparent)]`.

<a href="struct.BareFnArg.html" class="struct"
title="struct verus_syn::BareFnArg">BareFnArg</a>

An argument in a function type: the `usize` in `fn(usize) -> bool`.

<a href="struct.BareVariadic.html" class="struct"
title="struct verus_syn::BareVariadic">BareVariadic</a>

The variadic argument of a function pointer like `fn(usize, ...)`.

<a href="struct.BigAnd.html" class="struct"
title="struct verus_syn::BigAnd">BigAnd</a>

<a href="struct.BigAndExpr.html" class="struct"
title="struct verus_syn::BigAndExpr">BigAndExpr</a>

<a href="struct.BigOr.html" class="struct"
title="struct verus_syn::BigOr">BigOr</a>

<a href="struct.BigOrExpr.html" class="struct"
title="struct verus_syn::BigOrExpr">BigOrExpr</a>

<a href="struct.Block.html" class="struct"
title="struct verus_syn::Block">Block</a>

A braced block containing Rust statements.

<a href="struct.BoundLifetimes.html" class="struct"
title="struct verus_syn::BoundLifetimes">BoundLifetimes</a>

A set of bound lifetimes: `for<'a, 'b, 'c>`.

<a href="struct.BroadcastUse.html" class="struct"
title="struct verus_syn::BroadcastUse">BroadcastUse</a>

<a href="struct.Closed.html" class="struct"
title="struct verus_syn::Closed">Closed</a>

<a href="struct.ClosureArg.html" class="struct"
title="struct verus_syn::ClosureArg">ClosureArg</a>

<a href="struct.ConstParam.html" class="struct"
title="struct verus_syn::ConstParam">ConstParam</a>

A const generic parameter: `const LENGTH: usize`.

<a href="struct.Constraint.html" class="struct"
title="struct verus_syn::Constraint">Constraint</a>

An associated type bound: `Iterator<Item: Display>`.

<a href="struct.DataEnum.html" class="struct"
title="struct verus_syn::DataEnum">DataEnum</a>

An enum input to a `proc_macro_derive` macro.

<a href="struct.DataStruct.html" class="struct"
title="struct verus_syn::DataStruct">DataStruct</a>

A struct input to a `proc_macro_derive` macro.

<a href="struct.DataUnion.html" class="struct"
title="struct verus_syn::DataUnion">DataUnion</a>

An untagged union input to a `proc_macro_derive` macro.

<a href="struct.Decreases.html" class="struct"
title="struct verus_syn::Decreases">Decreases</a>

<a href="struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::DefaultEnsures">DefaultEnsures</a>

<a href="struct.DeriveInput.html" class="struct"
title="struct verus_syn::DeriveInput">DeriveInput</a>

Data structure sent to a `proc_macro_derive` macro.

<a href="struct.Ensures.html" class="struct"
title="struct verus_syn::Ensures">Ensures</a>

<a href="struct.Error.html" class="struct"
title="struct verus_syn::Error">Error</a>

Error returned when a Syn parser cannot parse the input tokens.

<a href="struct.ExprArray.html" class="struct"
title="struct verus_syn::ExprArray">ExprArray</a>

A slice literal expression: `[a, b, c, d]`.

<a href="struct.ExprAssign.html" class="struct"
title="struct verus_syn::ExprAssign">ExprAssign</a>

An assignment expression: `a = compute()`.

<a href="struct.ExprAsync.html" class="struct"
title="struct verus_syn::ExprAsync">ExprAsync</a>

An async block: `async { ... }`.

<a href="struct.ExprAwait.html" class="struct"
title="struct verus_syn::ExprAwait">ExprAwait</a>

An await expression: `fut.await`.

<a href="struct.ExprBinary.html" class="struct"
title="struct verus_syn::ExprBinary">ExprBinary</a>

A binary operation: `a + b`, `a += b`.

<a href="struct.ExprBlock.html" class="struct"
title="struct verus_syn::ExprBlock">ExprBlock</a>

A blocked scope: `{ ... }`.

<a href="struct.ExprBreak.html" class="struct"
title="struct verus_syn::ExprBreak">ExprBreak</a>

A `break`, with an optional label to break and an optional expression.

<a href="struct.ExprCall.html" class="struct"
title="struct verus_syn::ExprCall">ExprCall</a>

A function call expression: `invoke(a, b)`.

<a href="struct.ExprCast.html" class="struct"
title="struct verus_syn::ExprCast">ExprCast</a>

A cast expression: `foo as f64`.

<a href="struct.ExprClosure.html" class="struct"
title="struct verus_syn::ExprClosure">ExprClosure</a>

A closure expression: `|a, b| a + b`.

<a href="struct.ExprConst.html" class="struct"
title="struct verus_syn::ExprConst">ExprConst</a>

A const block: `const { ... }`.

<a href="struct.ExprContinue.html" class="struct"
title="struct verus_syn::ExprContinue">ExprContinue</a>

A `continue`, with an optional label.

<a href="struct.ExprField.html" class="struct"
title="struct verus_syn::ExprField">ExprField</a>

Access of a named struct field (`obj.k`) or unnamed tuple struct field
(`obj.0`).

<a href="struct.ExprForLoop.html" class="struct"
title="struct verus_syn::ExprForLoop">ExprForLoop</a>

A for loop: `for pat in expr { ... }`.

<a href="struct.ExprGetField.html" class="struct"
title="struct verus_syn::ExprGetField">ExprGetField</a>

<a href="struct.ExprGroup.html" class="struct"
title="struct verus_syn::ExprGroup">ExprGroup</a>

An expression contained within invisible delimiters.

<a href="struct.ExprHas.html" class="struct"
title="struct verus_syn::ExprHas">ExprHas</a>

<a href="struct.ExprHasNot.html" class="struct"
title="struct verus_syn::ExprHasNot">ExprHasNot</a>

<a href="struct.ExprIf.html" class="struct"
title="struct verus_syn::ExprIf">ExprIf</a>

An `if` expression with an optional `else` block:
`if expr { ... } else { ... }`.

<a href="struct.ExprIndex.html" class="struct"
title="struct verus_syn::ExprIndex">ExprIndex</a>

A square bracketed indexing expression: `vector[2]`.

<a href="struct.ExprInfer.html" class="struct"
title="struct verus_syn::ExprInfer">ExprInfer</a>

The inferred value of a const generic argument, denoted `_`.

<a href="struct.ExprIs.html" class="struct"
title="struct verus_syn::ExprIs">ExprIs</a>

<a href="struct.ExprIsNot.html" class="struct"
title="struct verus_syn::ExprIsNot">ExprIsNot</a>

<a href="struct.ExprLet.html" class="struct"
title="struct verus_syn::ExprLet">ExprLet</a>

A `let` guard: `let Some(x) = opt`.

<a href="struct.ExprLit.html" class="struct"
title="struct verus_syn::ExprLit">ExprLit</a>

A literal in place of an expression: `1`, `"foo"`.

<a href="struct.ExprLoop.html" class="struct"
title="struct verus_syn::ExprLoop">ExprLoop</a>

Conditionless loop: `loop { ... }`.

<a href="struct.ExprMacro.html" class="struct"
title="struct verus_syn::ExprMacro">ExprMacro</a>

A macro invocation expression: `format!("{}", q)`.

<a href="struct.ExprMatch.html" class="struct"
title="struct verus_syn::ExprMatch">ExprMatch</a>

A `match` expression: `match n { Some(n) => {}, None => {} }`.

<a href="struct.ExprMatches.html" class="struct"
title="struct verus_syn::ExprMatches">ExprMatches</a>

<a href="struct.ExprMethodCall.html" class="struct"
title="struct verus_syn::ExprMethodCall">ExprMethodCall</a>

A method call expression: `x.foo::<T>(a, b)`.

<a href="struct.ExprParen.html" class="struct"
title="struct verus_syn::ExprParen">ExprParen</a>

A parenthesized expression: `(a + b)`.

<a href="struct.ExprPath.html" class="struct"
title="struct verus_syn::ExprPath">ExprPath</a>

A path like `std::mem::replace` possibly containing generic parameters
and a qualified self-type.

<a href="struct.ExprRange.html" class="struct"
title="struct verus_syn::ExprRange">ExprRange</a>

A range expression: `1..2`, `1..`, `..2`, `1..=2`, `..=2`.

<a href="struct.ExprRawAddr.html" class="struct"
title="struct verus_syn::ExprRawAddr">ExprRawAddr</a>

Address-of operation: `&raw const place` or `&raw mut place`.

<a href="struct.ExprReference.html" class="struct"
title="struct verus_syn::ExprReference">ExprReference</a>

A referencing operation: `&a` or `&mut a`.

<a href="struct.ExprRepeat.html" class="struct"
title="struct verus_syn::ExprRepeat">ExprRepeat</a>

An array literal constructed from one repeated element: `[0u8; N]`.

<a href="struct.ExprReturn.html" class="struct"
title="struct verus_syn::ExprReturn">ExprReturn</a>

A `return`, with an optional value to be returned.

<a href="struct.ExprStruct.html" class="struct"
title="struct verus_syn::ExprStruct">ExprStruct</a>

A struct literal expression: `Point { x: 1, y: 1 }`.

<a href="struct.ExprTry.html" class="struct"
title="struct verus_syn::ExprTry">ExprTry</a>

A try-expression: `expr?`.

<a href="struct.ExprTryBlock.html" class="struct"
title="struct verus_syn::ExprTryBlock">ExprTryBlock</a>

A try block: `try { ... }`.

<a href="struct.ExprTuple.html" class="struct"
title="struct verus_syn::ExprTuple">ExprTuple</a>

A tuple expression: `(a, b, c, d)`.

<a href="struct.ExprUnary.html" class="struct"
title="struct verus_syn::ExprUnary">ExprUnary</a>

A unary operation: `!x`, `*x`.

<a href="struct.ExprUnsafe.html" class="struct"
title="struct verus_syn::ExprUnsafe">ExprUnsafe</a>

An unsafe block: `unsafe { ... }`.

<a href="struct.ExprWhile.html" class="struct"
title="struct verus_syn::ExprWhile">ExprWhile</a>

A while loop: `while expr { ... }`.

<a href="struct.ExprYield.html" class="struct"
title="struct verus_syn::ExprYield">ExprYield</a>

A yield expression: `yield expr`.

<a href="struct.Field.html" class="struct"
title="struct verus_syn::Field">Field</a>

A field of a struct or enum variant.

<a href="struct.FieldPat.html" class="struct"
title="struct verus_syn::FieldPat">FieldPat</a>

A single field in a struct pattern.

<a href="struct.FieldValue.html" class="struct"
title="struct verus_syn::FieldValue">FieldValue</a>

A field-value pair in a struct literal.

<a href="struct.FieldsNamed.html" class="struct"
title="struct verus_syn::FieldsNamed">FieldsNamed</a>

Named fields of a struct or struct variant such as
`Point { x: f64, y: f64 }`.

<a href="struct.FieldsUnnamed.html" class="struct"
title="struct verus_syn::FieldsUnnamed">FieldsUnnamed</a>

Unnamed fields of a tuple struct or tuple variant such as `Some(T)`.

<a href="struct.File.html" class="struct"
title="struct verus_syn::File">File</a>

A complete file of Rust source code.

<a href="struct.FnArg.html" class="struct"
title="struct verus_syn::FnArg">FnArg</a>

<a href="struct.FnProofArg.html" class="struct"
title="struct verus_syn::FnProofArg">FnProofArg</a>

<a href="struct.FnProofOptions.html" class="struct"
title="struct verus_syn::FnProofOptions">FnProofOptions</a>

<a href="struct.ForeignItemFn.html" class="struct"
title="struct verus_syn::ForeignItemFn">ForeignItemFn</a>

A foreign function in an `extern` block.

<a href="struct.ForeignItemMacro.html" class="struct"
title="struct verus_syn::ForeignItemMacro">ForeignItemMacro</a>

A macro invocation within an extern block.

<a href="struct.ForeignItemStatic.html" class="struct"
title="struct verus_syn::ForeignItemStatic">ForeignItemStatic</a>

A foreign static item in an `extern` block: `static ext: u8`.

<a href="struct.ForeignItemType.html" class="struct"
title="struct verus_syn::ForeignItemType">ForeignItemType</a>

A foreign type in an `extern` block: `type void`.

<a href="struct.Generics.html" class="struct"
title="struct verus_syn::Generics">Generics</a>

Lifetimes and type parameters attached to a declaration of a function,
enum, trait, etc.

<a href="struct.Global.html" class="struct"
title="struct verus_syn::Global">Global</a>

<a href="struct.GlobalLayout.html" class="struct"
title="struct verus_syn::GlobalLayout">GlobalLayout</a>

<a href="struct.GlobalSizeOf.html" class="struct"
title="struct verus_syn::GlobalSizeOf">GlobalSizeOf</a>

<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

A word of Rust code, which may be a keyword or legal variable name.

<a href="struct.ImplGenerics.html" class="struct"
title="struct verus_syn::ImplGenerics">ImplGenerics</a>

Returned by `Generics::split_for_impl`.

<a href="struct.ImplItemConst.html" class="struct"
title="struct verus_syn::ImplItemConst">ImplItemConst</a>

An associated constant within an impl block.

<a href="struct.ImplItemFn.html" class="struct"
title="struct verus_syn::ImplItemFn">ImplItemFn</a>

An associated function within an impl block.

<a href="struct.ImplItemMacro.html" class="struct"
title="struct verus_syn::ImplItemMacro">ImplItemMacro</a>

A macro invocation within an impl block.

<a href="struct.ImplItemType.html" class="struct"
title="struct verus_syn::ImplItemType">ImplItemType</a>

An associated type within an impl block.

<a href="struct.Index.html" class="struct"
title="struct verus_syn::Index">Index</a>

The index of an unnamed tuple struct field.

<a href="struct.Invariant.html" class="struct"
title="struct verus_syn::Invariant">Invariant</a>

<a href="struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::InvariantEnsures">InvariantEnsures</a>

<a href="struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::InvariantExceptBreak">InvariantExceptBreak</a>

<a href="struct.InvariantNameSetAny.html" class="struct"
title="struct verus_syn::InvariantNameSetAny">InvariantNameSetAny</a>

<a href="struct.InvariantNameSetList.html" class="struct"
title="struct verus_syn::InvariantNameSetList">InvariantNameSetList</a>

<a href="struct.InvariantNameSetNone.html" class="struct"
title="struct verus_syn::InvariantNameSetNone">InvariantNameSetNone</a>

<a href="struct.InvariantNameSetSet.html" class="struct"
title="struct verus_syn::InvariantNameSetSet">InvariantNameSetSet</a>

<a href="struct.ItemBroadcastGroup.html" class="struct"
title="struct verus_syn::ItemBroadcastGroup">ItemBroadcastGroup</a>

<a href="struct.ItemConst.html" class="struct"
title="struct verus_syn::ItemConst">ItemConst</a>

A constant item: `const MAX: u16 = 65535`.

<a href="struct.ItemEnum.html" class="struct"
title="struct verus_syn::ItemEnum">ItemEnum</a>

An enum definition: `enum Foo<A, B> { A(A), B(B) }`.

<a href="struct.ItemExternCrate.html" class="struct"
title="struct verus_syn::ItemExternCrate">ItemExternCrate</a>

An `extern crate` item: `extern crate serde`.

<a href="struct.ItemFn.html" class="struct"
title="struct verus_syn::ItemFn">ItemFn</a>

A free-standing function: `fn process(n: usize) -> Result<()> { ... }`.

<a href="struct.ItemForeignMod.html" class="struct"
title="struct verus_syn::ItemForeignMod">ItemForeignMod</a>

A block of foreign items: `extern "C" { ... }`.

<a href="struct.ItemImpl.html" class="struct"
title="struct verus_syn::ItemImpl">ItemImpl</a>

An impl block providing trait or associated items:
`impl<A> Trait for Data<A> { ... }`.

<a href="struct.ItemMacro.html" class="struct"
title="struct verus_syn::ItemMacro">ItemMacro</a>

A macro invocation, which includes `macro_rules!` definitions.

<a href="struct.ItemMod.html" class="struct"
title="struct verus_syn::ItemMod">ItemMod</a>

A module or module declaration: `mod m` or `mod m { ... }`.

<a href="struct.ItemStatic.html" class="struct"
title="struct verus_syn::ItemStatic">ItemStatic</a>

A static item: `static BIKE: Shed = Shed(42)`.

<a href="struct.ItemStruct.html" class="struct"
title="struct verus_syn::ItemStruct">ItemStruct</a>

A struct definition: `struct Foo<A> { x: A }`.

<a href="struct.ItemTrait.html" class="struct"
title="struct verus_syn::ItemTrait">ItemTrait</a>

A trait definition: `pub trait Iterator { ... }`.

<a href="struct.ItemTraitAlias.html" class="struct"
title="struct verus_syn::ItemTraitAlias">ItemTraitAlias</a>

A trait alias: `pub trait SharableIterator = Iterator + Sync`.

<a href="struct.ItemType.html" class="struct"
title="struct verus_syn::ItemType">ItemType</a>

A type alias: `type Result<T> = std::result::Result<T, MyError>`.

<a href="struct.ItemUnion.html" class="struct"
title="struct verus_syn::ItemUnion">ItemUnion</a>

A union definition: `union Foo<A, B> { x: A, y: B }`.

<a href="struct.ItemUse.html" class="struct"
title="struct verus_syn::ItemUse">ItemUse</a>

A use declaration: `use std::collections::HashMap`.

<a href="struct.Label.html" class="struct"
title="struct verus_syn::Label">Label</a>

A lifetime labeling a `for`, `while`, or `loop`.

<a href="struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>

A Rust lifetime: `'a`.

<a href="struct.LifetimeParam.html" class="struct"
title="struct verus_syn::LifetimeParam">LifetimeParam</a>

A lifetime definition: `'a: 'b + 'c + 'd`.

<a href="struct.LitBool.html" class="struct"
title="struct verus_syn::LitBool">LitBool</a>

A boolean literal: `true` or `false`.

<a href="struct.LitByte.html" class="struct"
title="struct verus_syn::LitByte">LitByte</a>

A byte literal: `b'f'`.

<a href="struct.LitByteStr.html" class="struct"
title="struct verus_syn::LitByteStr">LitByteStr</a>

A byte string literal: `b"foo"`.

<a href="struct.LitCStr.html" class="struct"
title="struct verus_syn::LitCStr">LitCStr</a>

A nul-terminated C-string literal: `c"foo"`.

<a href="struct.LitChar.html" class="struct"
title="struct verus_syn::LitChar">LitChar</a>

A character literal: `'a'`.

<a href="struct.LitFloat.html" class="struct"
title="struct verus_syn::LitFloat">LitFloat</a>

A floating point literal: `1f64` or `1.0e10f64`.

<a href="struct.LitInt.html" class="struct"
title="struct verus_syn::LitInt">LitInt</a>

An integer literal: `1` or `1u16`.

<a href="struct.LitStr.html" class="struct"
title="struct verus_syn::LitStr">LitStr</a>

A UTF-8 string literal: `"foo"`.

<a href="struct.Local.html" class="struct"
title="struct verus_syn::Local">Local</a>

A local `let` binding: `let x: u64 = s.parse()?;`.

<a href="struct.LocalInit.html" class="struct"
title="struct verus_syn::LocalInit">LocalInit</a>

The expression assigned in a local `let` binding, including optional
diverging `else` block.

<a href="struct.LoopSpec.html" class="struct"
title="struct verus_syn::LoopSpec">LoopSpec</a>

<a href="struct.Macro.html" class="struct"
title="struct verus_syn::Macro">Macro</a>

A macro invocation: `println!("{}", mac)`.

<a href="struct.MatchesOpExpr.html" class="struct"
title="struct verus_syn::MatchesOpExpr">MatchesOpExpr</a>

<a href="struct.MetaList.html" class="struct"
title="struct verus_syn::MetaList">MetaList</a>

A structured list within an attribute, like `derive(Copy, Clone)`.

<a href="struct.MetaNameValue.html" class="struct"
title="struct verus_syn::MetaNameValue">MetaNameValue</a>

A name-value pair within an attribute, like `feature = "nightly"`.

<a href="struct.ModeExec.html" class="struct"
title="struct verus_syn::ModeExec">ModeExec</a>

<a href="struct.ModeGhost.html" class="struct"
title="struct verus_syn::ModeGhost">ModeGhost</a>

<a href="struct.ModeProof.html" class="struct"
title="struct verus_syn::ModeProof">ModeProof</a>

<a href="struct.ModeProofAxiom.html" class="struct"
title="struct verus_syn::ModeProofAxiom">ModeProofAxiom</a>

<a href="struct.ModeSpec.html" class="struct"
title="struct verus_syn::ModeSpec">ModeSpec</a>

<a href="struct.ModeSpecChecked.html" class="struct"
title="struct verus_syn::ModeSpecChecked">ModeSpecChecked</a>

<a href="struct.ModeTracked.html" class="struct"
title="struct verus_syn::ModeTracked">ModeTracked</a>

<a href="struct.Open.html" class="struct"
title="struct verus_syn::Open">Open</a>

<a href="struct.OpenRestricted.html" class="struct"
title="struct verus_syn::OpenRestricted">OpenRestricted</a>

<a href="struct.ParenthesizedGenericArguments.html" class="struct"
title="struct verus_syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>

Arguments of a function path segment: the `(A, B) -> C` in
`Fn(A,B) -> C`.

<a href="struct.PatConst.html" class="struct"
title="struct verus_syn::PatConst">PatConst</a>

A const block: `const { ... }`.

<a href="struct.PatIdent.html" class="struct"
title="struct verus_syn::PatIdent">PatIdent</a>

A pattern that binds a new variable: `ref mut binding @ SUBPATTERN`.

<a href="struct.PatLit.html" class="struct"
title="struct verus_syn::PatLit">PatLit</a>

A literal in place of an expression: `1`, `"foo"`.

<a href="struct.PatMacro.html" class="struct"
title="struct verus_syn::PatMacro">PatMacro</a>

A macro invocation expression: `format!("{}", q)`.

<a href="struct.PatOr.html" class="struct"
title="struct verus_syn::PatOr">PatOr</a>

A pattern that matches any one of a set of cases.

<a href="struct.PatParen.html" class="struct"
title="struct verus_syn::PatParen">PatParen</a>

A parenthesized pattern: `(A | B)`.

<a href="struct.PatPath.html" class="struct"
title="struct verus_syn::PatPath">PatPath</a>

A path like `std::mem::replace` possibly containing generic parameters
and a qualified self-type.

<a href="struct.PatRange.html" class="struct"
title="struct verus_syn::PatRange">PatRange</a>

A range expression: `1..2`, `1..`, `..2`, `1..=2`, `..=2`.

<a href="struct.PatReference.html" class="struct"
title="struct verus_syn::PatReference">PatReference</a>

A reference pattern: `&mut var`.

<a href="struct.PatRest.html" class="struct"
title="struct verus_syn::PatRest">PatRest</a>

The dots in a tuple or slice pattern: `[0, 1, ..]`.

<a href="struct.PatSlice.html" class="struct"
title="struct verus_syn::PatSlice">PatSlice</a>

A dynamically sized slice pattern: `[a, b, ref i @ .., y, z]`.

<a href="struct.PatStruct.html" class="struct"
title="struct verus_syn::PatStruct">PatStruct</a>

A struct or struct variant pattern: `Variant { x, y, .. }`.

<a href="struct.PatTuple.html" class="struct"
title="struct verus_syn::PatTuple">PatTuple</a>

A tuple pattern: `(a, b)`.

<a href="struct.PatTupleStruct.html" class="struct"
title="struct verus_syn::PatTupleStruct">PatTupleStruct</a>

A tuple struct or tuple variant pattern: `Variant(x, y, .., z)`.

<a href="struct.PatType.html" class="struct"
title="struct verus_syn::PatType">PatType</a>

A type ascription pattern: `foo: f64`.

<a href="struct.PatWild.html" class="struct"
title="struct verus_syn::PatWild">PatWild</a>

A pattern that matches any value: `_`.

<a href="struct.Path.html" class="struct"
title="struct verus_syn::Path">Path</a>

A path at which a named item is exported (e.g.
`std::collections::HashMap`).

<a href="struct.PathSegment.html" class="struct"
title="struct verus_syn::PathSegment">PathSegment</a>

A segment of a path together with any path arguments on that segment.

<a href="struct.PreciseCapture.html" class="struct"
title="struct verus_syn::PreciseCapture">PreciseCapture</a>

Precise capturing bound: the ‘use\<…\>’ in `impl Trait + use<'a, T>`.

<a href="struct.PredicateLifetime.html" class="struct"
title="struct verus_syn::PredicateLifetime">PredicateLifetime</a>

A lifetime predicate in a `where` clause: `'a: 'b + 'c`.

<a href="struct.PredicateType.html" class="struct"
title="struct verus_syn::PredicateType">PredicateType</a>

A type predicate in a `where` clause: `for<'c> Foo<'c>: Trait<'c>`.

<a href="struct.Prover.html" class="struct"
title="struct verus_syn::Prover">Prover</a>

<a href="struct.QSelf.html" class="struct"
title="struct verus_syn::QSelf">QSelf</a>

The explicit Self type in a qualified path: the `T` in
`<T as Display>::fmt`.

<a href="struct.Receiver.html" class="struct"
title="struct verus_syn::Receiver">Receiver</a>

The `self` argument of an associated method.

<a href="struct.Recommends.html" class="struct"
title="struct verus_syn::Recommends">Recommends</a>

<a href="struct.Requires.html" class="struct"
title="struct verus_syn::Requires">Requires</a>

<a href="struct.Returns.html" class="struct"
title="struct verus_syn::Returns">Returns</a>

<a href="struct.RevealHide.html" class="struct"
title="struct verus_syn::RevealHide">RevealHide</a>

<a href="struct.Signature.html" class="struct"
title="struct verus_syn::Signature">Signature</a>

A function signature in a trait or implementation:
`unsafe fn initialize(&self)`.

<a href="struct.SignatureDecreases.html" class="struct"
title="struct verus_syn::SignatureDecreases">SignatureDecreases</a>

<a href="struct.SignatureInvariants.html" class="struct"
title="struct verus_syn::SignatureInvariants">SignatureInvariants</a>

<a href="struct.SignatureSpec.html" class="struct"
title="struct verus_syn::SignatureSpec">SignatureSpec</a>

<a href="struct.SignatureSpecAttr.html" class="struct"
title="struct verus_syn::SignatureSpecAttr">SignatureSpecAttr</a>

<a href="struct.SignatureUnwind.html" class="struct"
title="struct verus_syn::SignatureUnwind">SignatureUnwind</a>

<a href="struct.Specification.html" class="struct"
title="struct verus_syn::Specification">Specification</a>

<a href="struct.StmtMacro.html" class="struct"
title="struct verus_syn::StmtMacro">StmtMacro</a>

A macro invocation in statement position.

<a href="struct.TraitBound.html" class="struct"
title="struct verus_syn::TraitBound">TraitBound</a>

A trait used as a bound on a type parameter.

<a href="struct.TraitItemConst.html" class="struct"
title="struct verus_syn::TraitItemConst">TraitItemConst</a>

An associated constant within the definition of a trait.

<a href="struct.TraitItemFn.html" class="struct"
title="struct verus_syn::TraitItemFn">TraitItemFn</a>

An associated function within the definition of a trait.

<a href="struct.TraitItemMacro.html" class="struct"
title="struct verus_syn::TraitItemMacro">TraitItemMacro</a>

A macro invocation within the definition of a trait.

<a href="struct.TraitItemType.html" class="struct"
title="struct verus_syn::TraitItemType">TraitItemType</a>

An associated type within the definition of a trait.

<a href="struct.Turbofish.html" class="struct"
title="struct verus_syn::Turbofish">Turbofish</a>

Returned by `TypeGenerics::as_turbofish`.

<a href="struct.TypeArray.html" class="struct"
title="struct verus_syn::TypeArray">TypeArray</a>

A fixed size array type: `[T; n]`.

<a href="struct.TypeBareFn.html" class="struct"
title="struct verus_syn::TypeBareFn">TypeBareFn</a>

A bare function type: `fn(usize) -> bool`.

<a href="struct.TypeFnProof.html" class="struct"
title="struct verus_syn::TypeFnProof">TypeFnProof</a>

A proof_fn type:
`proof_fn<'a, F>[ReqEns<R>, Copy, Send, Sync](tracked usize) -> tracked bool`
Parsed similarly to TypeBareFn

<a href="struct.TypeFnSpec.html" class="struct"
title="struct verus_syn::TypeFnSpec">TypeFnSpec</a>

A FnSpec type: `FnSpec(usize) -> bool`. Parsed similarly to TypeBareFn

<a href="struct.TypeGenerics.html" class="struct"
title="struct verus_syn::TypeGenerics">TypeGenerics</a>

Returned by `Generics::split_for_impl`.

<a href="struct.TypeGroup.html" class="struct"
title="struct verus_syn::TypeGroup">TypeGroup</a>

A type contained within invisible delimiters.

<a href="struct.TypeImplTrait.html" class="struct"
title="struct verus_syn::TypeImplTrait">TypeImplTrait</a>

An `impl Bound1 + Bound2 + Bound3` type where `Bound` is a trait or a
lifetime.

<a href="struct.TypeInfer.html" class="struct"
title="struct verus_syn::TypeInfer">TypeInfer</a>

Indication that a type should be inferred by the compiler: `_`.

<a href="struct.TypeMacro.html" class="struct"
title="struct verus_syn::TypeMacro">TypeMacro</a>

A macro in the type position.

<a href="struct.TypeNever.html" class="struct"
title="struct verus_syn::TypeNever">TypeNever</a>

The never type: `!`.

<a href="struct.TypeParam.html" class="struct"
title="struct verus_syn::TypeParam">TypeParam</a>

A generic type parameter: `T: Into<String>`.

<a href="struct.TypeParen.html" class="struct"
title="struct verus_syn::TypeParen">TypeParen</a>

A parenthesized type equivalent to the inner type.

<a href="struct.TypePath.html" class="struct"
title="struct verus_syn::TypePath">TypePath</a>

A path like `std::slice::Iter`, optionally qualified with a self-type as
in `<Vec<T> as SomeTrait>::Associated`.

<a href="struct.TypePtr.html" class="struct"
title="struct verus_syn::TypePtr">TypePtr</a>

A raw pointer type: `*const T` or `*mut T`.

<a href="struct.TypeReference.html" class="struct"
title="struct verus_syn::TypeReference">TypeReference</a>

A reference type: `&'a T` or `&'a mut T`.

<a href="struct.TypeSlice.html" class="struct"
title="struct verus_syn::TypeSlice">TypeSlice</a>

A dynamically sized slice type: `[T]`.

<a href="struct.TypeTraitObject.html" class="struct"
title="struct verus_syn::TypeTraitObject">TypeTraitObject</a>

A trait object type `dyn Bound1 + Bound2 + Bound3` where `Bound` is a
trait or a lifetime.

<a href="struct.TypeTuple.html" class="struct"
title="struct verus_syn::TypeTuple">TypeTuple</a>

A tuple type: `(A, B, C, String)`.

<a href="struct.Uninterp.html" class="struct"
title="struct verus_syn::Uninterp">Uninterp</a>

<a href="struct.UseGlob.html" class="struct"
title="struct verus_syn::UseGlob">UseGlob</a>

A glob import in a `use` item: `*`.

<a href="struct.UseGroup.html" class="struct"
title="struct verus_syn::UseGroup">UseGroup</a>

A braced group of imports in a `use` item: `{A, B, C}`.

<a href="struct.UseName.html" class="struct"
title="struct verus_syn::UseName">UseName</a>

An identifier imported by a `use` item: `HashMap`.

<a href="struct.UsePath.html" class="struct"
title="struct verus_syn::UsePath">UsePath</a>

A path prefix of imports in a `use` item: `std::...`.

<a href="struct.UseRename.html" class="struct"
title="struct verus_syn::UseRename">UseRename</a>

An renamed identifier imported by a `use` item: `HashMap as Map`.

<a href="struct.Variadic.html" class="struct"
title="struct verus_syn::Variadic">Variadic</a>

The variadic argument of a foreign function.

<a href="struct.Variant.html" class="struct"
title="struct verus_syn::Variant">Variant</a>

An enum variant.

<a href="struct.View.html" class="struct"
title="struct verus_syn::View">View</a>

<a href="struct.VisRestricted.html" class="struct"
title="struct verus_syn::VisRestricted">VisRestricted</a>

A visibility level restricted to some path: `pub(self)` or `pub(super)`
or `pub(crate)` or `pub(in some::module)`.

<a href="struct.WhereClause.html" class="struct"
title="struct verus_syn::WhereClause">WhereClause</a>

A `where` clause in a definition:
`where T: Deserialize<'de>, D: 'static`.

<a href="struct.WithSpecOnExpr.html" class="struct"
title="struct verus_syn::WithSpecOnExpr">WithSpecOnExpr</a>

<a href="struct.WithSpecOnFn.html" class="struct"
title="struct verus_syn::WithSpecOnFn">WithSpecOnFn</a>

## Enums<a href="#enums" class="anchor">§</a>

<a href="enum.AttrStyle.html" class="enum"
title="enum verus_syn::AttrStyle">AttrStyle</a>  
Distinguishes between attributes that decorate an item and attributes
that are contained within an item.

<a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>  
A binary operator: `+`, `+=`, `&`.

<a href="enum.CapturedParam.html" class="enum"
title="enum verus_syn::CapturedParam">CapturedParam</a>  
Single parameter in a precise capturing bound.

<a href="enum.Data.html" class="enum"
title="enum verus_syn::Data">Data</a>  
The storage of a struct, enum or union data structure.

<a href="enum.DataMode.html" class="enum"
title="enum verus_syn::DataMode">DataMode</a>  
<a href="enum.Expr.html" class="enum"
title="enum verus_syn::Expr">Expr</a>  
A Rust expression.

<a href="enum.FieldMutability.html" class="enum"
title="enum verus_syn::FieldMutability">FieldMutability</a>  
Unused, but reserved for RFC 3323 restrictions.

<a href="enum.Fields.html" class="enum"
title="enum verus_syn::Fields">Fields</a>  
Data stored within an enum variant or struct.

<a href="enum.FnArgKind.html" class="enum"
title="enum verus_syn::FnArgKind">FnArgKind</a>  
An argument in a function signature: the `n: usize` in `fn f(n: usize)`.

<a href="enum.FnMode.html" class="enum"
title="enum verus_syn::FnMode">FnMode</a>  
<a href="enum.ForeignItem.html" class="enum"
title="enum verus_syn::ForeignItem">ForeignItem</a>  
An item within an `extern` block.

<a href="enum.GenericArgument.html" class="enum"
title="enum verus_syn::GenericArgument">GenericArgument</a>  
An individual generic argument, like `'a`, `T`, or `Item = T`.

<a href="enum.GenericParam.html" class="enum"
title="enum verus_syn::GenericParam">GenericParam</a>  
A generic type parameter, lifetime, or const generic: `T: Into<String>`,
`'a: 'b`, `const LEN: usize`.

<a href="enum.GlobalInner.html" class="enum"
title="enum verus_syn::GlobalInner">GlobalInner</a>  
<a href="enum.ImplItem.html" class="enum"
title="enum verus_syn::ImplItem">ImplItem</a>  
An item within an impl block.

<a href="enum.ImplRestriction.html" class="enum"
title="enum verus_syn::ImplRestriction">ImplRestriction</a>  
Unused, but reserved for RFC 3323 restrictions.

<a href="enum.InvariantNameSet.html" class="enum"
title="enum verus_syn::InvariantNameSet">InvariantNameSet</a>  
<a href="enum.Item.html" class="enum"
title="enum verus_syn::Item">Item</a>  
Things that can appear directly inside of a module or scope.

<a href="enum.Lit.html" class="enum" title="enum verus_syn::Lit">Lit</a>  
A Rust literal such as a string or integer or boolean.

<a href="enum.MacroDelimiter.html" class="enum"
title="enum verus_syn::MacroDelimiter">MacroDelimiter</a>  
A grouping token that surrounds a macro body: `m!(...)` or `m!{...}` or
`m![...]`.

<a href="enum.MatchesOpToken.html" class="enum"
title="enum verus_syn::MatchesOpToken">MatchesOpToken</a>  
<a href="enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>  
A struct or tuple struct field accessed in a struct literal or field
expression.

<a href="enum.Meta.html" class="enum"
title="enum verus_syn::Meta">Meta</a>  
Content of a compile-time structured attribute.

<a href="enum.Mode.html" class="enum"
title="enum verus_syn::Mode">Mode</a>  
<a href="enum.Pat.html" class="enum" title="enum verus_syn::Pat">Pat</a>  
A pattern in a local binding, function signature, match expression, or
various other places.

<a href="enum.PathArguments.html" class="enum"
title="enum verus_syn::PathArguments">PathArguments</a>  
Angle bracketed or parenthesized arguments of a path segment.

<a href="enum.PointerMutability.html" class="enum"
title="enum verus_syn::PointerMutability">PointerMutability</a>  
Mutability of a raw pointer (`*const T`, `*mut T`), in which non-mutable
isn’t the implicit default.

<a href="enum.Publish.html" class="enum"
title="enum verus_syn::Publish">Publish</a>  
<a href="enum.RangeLimits.html" class="enum"
title="enum verus_syn::RangeLimits">RangeLimits</a>  
Limit types of a range, inclusive or exclusive.

<a href="enum.ReturnType.html" class="enum"
title="enum verus_syn::ReturnType">ReturnType</a>  
Return type of a function signature.

<a href="enum.StaticMutability.html" class="enum"
title="enum verus_syn::StaticMutability">StaticMutability</a>  
The mutability of an `Item::Static` or `ForeignItem::Static`.

<a href="enum.Stmt.html" class="enum"
title="enum verus_syn::Stmt">Stmt</a>  
A statement, usually ending in a semicolon.

<a href="enum.TraitBoundModifier.html" class="enum"
title="enum verus_syn::TraitBoundModifier">TraitBoundModifier</a>  
A modifier on a trait bound, currently only used for the `?` in
`?Sized`.

<a href="enum.TraitItem.html" class="enum"
title="enum verus_syn::TraitItem">TraitItem</a>  
An item declaration within the definition of a trait.

<a href="enum.Type.html" class="enum"
title="enum verus_syn::Type">Type</a>  
The possible types that a Rust value could have.

<a href="enum.TypeParamBound.html" class="enum"
title="enum verus_syn::TypeParamBound">TypeParamBound</a>  
A trait or lifetime used as a bound on a type parameter.

<a href="enum.UnOp.html" class="enum"
title="enum verus_syn::UnOp">UnOp</a>  
A unary operator: `*`, `!`, `-`.

<a href="enum.UseTree.html" class="enum"
title="enum verus_syn::UseTree">UseTree</a>  
A suffix of an import tree in a `use` item: `Type as Renamed` or `*`.

<a href="enum.Visibility.html" class="enum"
title="enum verus_syn::Visibility">Visibility</a>  
The visibility level of an item: inherited or `pub` or
`pub(restricted)`.

<a href="enum.WherePredicate.html" class="enum"
title="enum verus_syn::WherePredicate">WherePredicate</a>  
A single predicate in a `where` clause: `T: Deserialize<'de>`.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.parse.html" class="fn" title="fn verus_syn::parse">parse</a>

Parse tokens of source code into the chosen syntax tree node.

<a href="fn.parse2.html" class="fn"
title="fn verus_syn::parse2">parse2</a>

Parse a proc-macro2 token stream into the chosen syntax tree node.

<a href="fn.parse_file.html" class="fn"
title="fn verus_syn::parse_file">parse_file</a>

Parse the content of a file of Rust code.

<a href="fn.parse_str.html" class="fn"
title="fn verus_syn::parse_str">parse_str</a>

Parse a string of Rust code into the chosen syntax tree node.

<a href="fn.rejoin_tokens.html" class="fn"
title="fn verus_syn::rejoin_tokens">rejoin_tokens</a>

## Type Aliases<a href="#types" class="anchor">§</a>

<a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>  
The result of a Syn parser.

</div>

</div>
