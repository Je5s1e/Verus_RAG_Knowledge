<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Enum <span class="enum">Pat</span> Copy item path

<span class="sub-heading"><a href="../src/syn/pat.rs.html#17-104" class="src">Source</a>
</span>

</div>

``` rust
#[non_exhaustive]pub enum Pat {
Show 17 variants    Const(PatConst),
    Ident(PatIdent),
    Lit(PatLit),
    Macro(PatMacro),
    Or(PatOr),
    Paren(PatParen),
    Path(PatPath),
    Range(PatRange),
    Reference(PatReference),
    Rest(PatRest),
    Slice(PatSlice),
    Struct(PatStruct),
    Tuple(PatTuple),
    TupleStruct(PatTupleStruct),
    Type(PatType),
    Verbatim(TokenStream),
    Wild(PatWild),
}
```

Expand description

<div class="docblock">

A pattern in a local binding, function signature, match expression, or
various other places.

## <a href="#syntax-tree-enum" class="doc-anchor">§</a>Syntax tree enum

This type is a [syntax tree
enum](enum.Expr.html#syntax-tree-enums "enum syn::Expr").

</div>

## Variants (Non-exhaustive)<a href="#variants" class="anchor">§</a>

This enum is marked as non-exhaustive

<div class="docblock">

Non-exhaustive enums could have additional variants added in future.
Therefore, when matching against variants of non-exhaustive enums, an
extra wildcard arm must be added to account for any future variants.

</div>

<div class="variants">

<div id="variant.Const" class="section variant">

<a href="#variant.Const" class="anchor">§</a>

### Const(<a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">PatConst</a>)

</div>

<div class="docblock">

A const block: `const { ... }`.

</div>

<div id="variant.Ident" class="section variant">

<a href="#variant.Ident" class="anchor">§</a>

### Ident(<a href="struct.PatIdent.html" class="struct"
title="struct syn::PatIdent">PatIdent</a>)

</div>

<div class="docblock">

A pattern that binds a new variable: `ref mut binding @ SUBPATTERN`.

</div>

<div id="variant.Lit" class="section variant">

<a href="#variant.Lit" class="anchor">§</a>

### Lit(<a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">PatLit</a>)

</div>

<div class="docblock">

A literal pattern: `0`.

</div>

<div id="variant.Macro" class="section variant">

<a href="#variant.Macro" class="anchor">§</a>

### Macro(<a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">PatMacro</a>)

</div>

<div class="docblock">

A macro in pattern position.

</div>

<div id="variant.Or" class="section variant">

<a href="#variant.Or" class="anchor">§</a>

### Or(<a href="struct.PatOr.html" class="struct"
title="struct syn::PatOr">PatOr</a>)

</div>

<div class="docblock">

A pattern that matches any one of a set of cases.

</div>

<div id="variant.Paren" class="section variant">

<a href="#variant.Paren" class="anchor">§</a>

### Paren(<a href="struct.PatParen.html" class="struct"
title="struct syn::PatParen">PatParen</a>)

</div>

<div class="docblock">

A parenthesized pattern: `(A | B)`.

</div>

<div id="variant.Path" class="section variant">

<a href="#variant.Path" class="anchor">§</a>

### Path(<a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">PatPath</a>)

</div>

<div class="docblock">

A path pattern like `Color::Red`, optionally qualified with a self-type.

Unqualified path patterns can legally refer to variants, structs,
constants or associated constants. Qualified path patterns like
`<A>::B::C` and `<A as Trait>::B::C` can only legally refer to
associated constants.

</div>

<div id="variant.Range" class="section variant">

<a href="#variant.Range" class="anchor">§</a>

### Range(<a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">PatRange</a>)

</div>

<div class="docblock">

A range pattern: `1..=2`.

</div>

<div id="variant.Reference" class="section variant">

<a href="#variant.Reference" class="anchor">§</a>

### Reference(<a href="struct.PatReference.html" class="struct"
title="struct syn::PatReference">PatReference</a>)

</div>

<div class="docblock">

A reference pattern: `&mut var`.

</div>

<div id="variant.Rest" class="section variant">

<a href="#variant.Rest" class="anchor">§</a>

### Rest(<a href="struct.PatRest.html" class="struct"
title="struct syn::PatRest">PatRest</a>)

</div>

<div class="docblock">

The dots in a tuple or slice pattern: `[0, 1, ..]`.

</div>

<div id="variant.Slice" class="section variant">

<a href="#variant.Slice" class="anchor">§</a>

### Slice(<a href="struct.PatSlice.html" class="struct"
title="struct syn::PatSlice">PatSlice</a>)

</div>

<div class="docblock">

A dynamically sized slice pattern: `[a, b, ref i @ .., y, z]`.

</div>

<div id="variant.Struct" class="section variant">

<a href="#variant.Struct" class="anchor">§</a>

### Struct(<a href="struct.PatStruct.html" class="struct"
title="struct syn::PatStruct">PatStruct</a>)

</div>

<div class="docblock">

A struct or struct variant pattern: `Variant { x, y, .. }`.

</div>

<div id="variant.Tuple" class="section variant">

<a href="#variant.Tuple" class="anchor">§</a>

### Tuple(<a href="struct.PatTuple.html" class="struct"
title="struct syn::PatTuple">PatTuple</a>)

</div>

<div class="docblock">

A tuple pattern: `(a, b)`.

</div>

<div id="variant.TupleStruct" class="section variant">

<a href="#variant.TupleStruct" class="anchor">§</a>

### TupleStruct(<a href="struct.PatTupleStruct.html" class="struct"
title="struct syn::PatTupleStruct">PatTupleStruct</a>)

</div>

<div class="docblock">

A tuple struct or tuple variant pattern: `Variant(x, y, .., z)`.

</div>

<div id="variant.Type" class="section variant">

<a href="#variant.Type" class="anchor">§</a>

### Type(<a href="struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>)

</div>

<div class="docblock">

A type ascription pattern: `foo: f64`.

</div>

<div id="variant.Verbatim" class="section variant">

<a href="#variant.Verbatim" class="anchor">§</a>

### Verbatim(<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Tokens in pattern position not interpreted by Syn.

</div>

<div id="variant.Wild" class="section variant">

<a href="#variant.Wild" class="anchor">§</a>

### Wild(<a href="struct.PatWild.html" class="struct"
title="struct syn::PatWild">PatWild</a>)

</div>

<div class="docblock">

A pattern that matches any value: `_`.

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#266-387"
class="src rightside">Source</a><a href="#impl-Pat" class="anchor">§</a>

### impl <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.parse_single" class="section method">

<a href="../src/syn/pat.rs.html#291-334"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_single" class="fn">parse_single</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Parse a pattern that does *not* involve `|` at the top level.

This parser matches the behavior of the `$:pat_param` macro_rules
matcher, and on editions prior to Rust 2021, the behavior of `$:pat`.

In Rust syntax, some examples of where this syntax would occur are in
the argument pattern of functions and closures. Patterns using `|` are
not allowed to occur in these positions.

<div class="example-wrap compile_fail">

<a href="#" class="tooltip"
title="This example deliberately fails to compile">ⓘ</a>

``` rust
fn f(Some(_) | None: Option<T>) {
    let _ = |Some(_) | None: Option<T>| {};
    //       ^^^^^^^^^^^^^^^^^^^^^^^^^??? :(
}
```

</div>

<div class="example-wrap">

``` console
error: top-level or-patterns are not allowed in function parameters
 --> src/main.rs:1:6
  |
1 | fn f(Some(_) | None: Option<T>) {
  |      ^^^^^^^^^^^^^^ help: wrap the pattern in parentheses: `(Some(_) | None)`
```

</div>

</div>

<div id="method.parse_multi" class="section method">

<a href="../src/syn/pat.rs.html#337-339"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_multi" class="fn">parse_multi</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Parse a pattern, possibly involving `|`, but not a leading `|`.

</div>

<div id="method.parse_multi_with_leading_vert" class="section method">

<a href="../src/syn/pat.rs.html#383-386"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_multi_with_leading_vert"
class="fn">parse_multi_with_leading_vert</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Parse a pattern, possibly involving `|`, possibly including a leading
`|`.

This parser matches the behavior of the Rust 2021 edition’s `$:pat`
macro_rules matcher.

In Rust syntax, an example of where this syntax would occur is in the
pattern of a `match` arm, where the language permits an optional leading
`|`, although it is not idiomatic to write one there in handwritten
code.

<div class="example-wrap">

``` rust
match wat {
    | None | Some(false) => {}
    | Some(true) => {}
}
```

</div>

The compiler accepts it only to facilitate some situations in
macro-generated code where a macro author might need to write:

<div class="example-wrap">

``` rust
match $value {
    $(| $conditions1)* $(| $conditions2)* => $then
}
```

</div>

Expressing the same thing correctly in the case that either one (but not
both) of `$conditions1` and `$conditions2` might be empty, without
leading `|`, is complex.

Use
[`Pat::parse_multi`](enum.Pat.html#method.parse_multi "associated function syn::Pat::parse_multi")
instead if you are not intending to support macro-generated macro input.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Pat" class="section impl">

<a href="../src/syn/gen/clone.rs.html#1491-1513"
class="src rightside">Source</a><a href="#impl-Clone-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/syn/gen/clone.rs.html#1492-1512"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-Pat" class="section impl">

<a href="../src/syn/gen/debug.rs.html#2164-2191"
class="src rightside">Source</a><a href="#impl-Debug-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/syn/gen/debug.rs.html#2165-2190"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, formatter: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-From%3CExprConst%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CExprConst%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">PatConst</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprLit%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CExprLit%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-2" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">PatLit</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprMacro%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CExprMacro%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-3" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-3" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">PatMacro</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprPath%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CExprPath%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-6" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-6" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">PatPath</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprRange%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CExprRange%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-7" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-7" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">PatRange</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatIdent%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatIdent%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatIdent.html" class="struct"
title="struct syn::PatIdent">PatIdent</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-1" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatIdent.html" class="struct"
title="struct syn::PatIdent">PatIdent</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatOr%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatOr%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatOr.html" class="struct"
title="struct syn::PatOr">PatOr</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-4" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-4" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatOr.html" class="struct"
title="struct syn::PatOr">PatOr</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatParen%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatParen%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatParen.html" class="struct"
title="struct syn::PatParen">PatParen</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-5" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-5" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatParen.html" class="struct"
title="struct syn::PatParen">PatParen</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatReference%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatReference%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatReference.html" class="struct"
title="struct syn::PatReference">PatReference</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-8" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-8" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatReference.html" class="struct"
title="struct syn::PatReference">PatReference</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatRest%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatRest%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatRest.html" class="struct"
title="struct syn::PatRest">PatRest</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-9" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-9" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatRest.html" class="struct"
title="struct syn::PatRest">PatRest</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatSlice%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatSlice%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatSlice.html" class="struct"
title="struct syn::PatSlice">PatSlice</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-10" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-10" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatSlice.html" class="struct"
title="struct syn::PatSlice">PatSlice</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatStruct%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatStruct%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatStruct.html" class="struct"
title="struct syn::PatStruct">PatStruct</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-11" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-11" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatStruct.html" class="struct"
title="struct syn::PatStruct">PatStruct</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatTuple%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatTuple%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatTuple.html" class="struct"
title="struct syn::PatTuple">PatTuple</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-12" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-12" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatTuple.html" class="struct"
title="struct syn::PatTuple">PatTuple</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatTupleStruct%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatTupleStruct%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatTupleStruct.html" class="struct"
title="struct syn::PatTupleStruct">PatTupleStruct</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-13" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-13" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatTupleStruct.html" class="struct"
title="struct syn::PatTupleStruct">PatTupleStruct</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatType%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatType%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-14" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-14" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CPatWild%3E-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-From%3CPatWild%3E-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.PatWild.html" class="struct"
title="struct syn::PatWild">PatWild</a>\> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.from-15" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.from-15" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.PatWild.html" class="struct"
title="struct syn::PatWild">PatWild</a>) -\> <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-Hash-for-Pat" class="section impl">

<a href="../src/syn/gen/hash.rs.html#1876-1952"
class="src rightside">Source</a><a href="#impl-Hash-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/syn/gen/hash.rs.html#1877-1951"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<H\>(&self, state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>,

</div>

</div>

<div class="docblock">

Feeds this value into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash)

</div>

<div id="method.hash_slice" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.3.0">1.3.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/hash/mod.rs.html#235-237"
class="src">Source</a></span><a href="#method.hash_slice" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice"
class="fn">hash_slice</a>\<H\>(data: &\[Self\], state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Feeds a slice of this type into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice)

</div>

</div>

<div id="impl-PartialEq-for-Pat" class="section impl">

<a href="../src/syn/gen/eq.rs.html#1474-1503"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/syn/gen/eq.rs.html#1475-1502"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-ToTokens-for-Pat" class="section impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#impl-ToTokens-for-Pat" class="anchor">§</a>

### impl <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/syn/pat.rs.html#17-104" class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Eq-for-Pat" class="section impl">

<a href="../src/syn/gen/eq.rs.html#1471"
class="src rightside">Source</a><a href="#impl-Eq-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Pat" class="section impl">

<a href="#impl-Freeze-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div id="impl-RefUnwindSafe-for-Pat" class="section impl">

<a href="#impl-RefUnwindSafe-for-Pat" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div id="impl-Send-for-Pat" class="section impl">

<a href="#impl-Send-for-Pat" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div id="impl-Sync-for-Pat" class="section impl">

<a href="#impl-Sync-for-Pat" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div id="impl-Unpin-for-Pat" class="section impl">

<a href="#impl-Unpin-for-Pat" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

<div id="impl-UnwindSafe-for-Pat" class="section impl">

<a href="#impl-UnwindSafe-for-Pat" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from-16" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-16" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-Spanned-for-T" class="section impl">

<a href="../src/syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="spanned/trait.Spanned.html" class="trait"
title="trait syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span" class="section method trait-impl">

<a href="../src/syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span" class="anchor">§</a>

#### fn <a href="spanned/trait.Spanned.html#tymethod.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
if this node is empty.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
