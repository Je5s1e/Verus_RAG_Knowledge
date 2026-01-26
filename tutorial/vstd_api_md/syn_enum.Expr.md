<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Enum <span class="enum">Expr</span> Copy item path

<span class="sub-heading"><a href="../src/syn/expr.rs.html#37-269" class="src">Source</a>
</span>

</div>

``` rust
#[non_exhaustive]pub enum Expr {
Show 40 variants    Array(ExprArray),
    Assign(ExprAssign),
    Async(ExprAsync),
    Await(ExprAwait),
    Binary(ExprBinary),
    Block(ExprBlock),
    Break(ExprBreak),
    Call(ExprCall),
    Cast(ExprCast),
    Closure(ExprClosure),
    Const(ExprConst),
    Continue(ExprContinue),
    Field(ExprField),
    ForLoop(ExprForLoop),
    Group(ExprGroup),
    If(ExprIf),
    Index(ExprIndex),
    Infer(ExprInfer),
    Let(ExprLet),
    Lit(ExprLit),
    Loop(ExprLoop),
    Macro(ExprMacro),
    Match(ExprMatch),
    MethodCall(ExprMethodCall),
    Paren(ExprParen),
    Path(ExprPath),
    Range(ExprRange),
    RawAddr(ExprRawAddr),
    Reference(ExprReference),
    Repeat(ExprRepeat),
    Return(ExprReturn),
    Struct(ExprStruct),
    Try(ExprTry),
    TryBlock(ExprTryBlock),
    Tuple(ExprTuple),
    Unary(ExprUnary),
    Unsafe(ExprUnsafe),
    Verbatim(TokenStream),
    While(ExprWhile),
    Yield(ExprYield),
}
```

Expand description

<div class="docblock">

A Rust expression.

*This type is available only if Syn is built with the `"derive"` or
`"full"` feature, but most of the variants are not available unless
“full” is enabled.*

## <a href="#syntax-tree-enums" class="doc-anchor">§</a>Syntax tree enums

This type is a syntax tree enum. In Syn this and other syntax tree enums
are designed to be traversed using the following rebinding idiom.

<div class="example-wrap">

``` rust
let expr: Expr = /* ... */;
match expr {
    Expr::MethodCall(expr) => {
        /* ... */
    }
    Expr::Cast(expr) => {
        /* ... */
    }
    Expr::If(expr) => {
        /* ... */
    }

    /* ... */
```

</div>

We begin with a variable `expr` of type `Expr` that has no fields
(because it is an enum), and by matching on it and rebinding a variable
with the same name `expr` we effectively imbue our variable with all of
the data fields provided by the variant that it turned out to be. So for
example above if we ended up in the `MethodCall` case then we get to use
`expr.receiver`, `expr.args` etc; if we ended up in the `If` case we get
to use `expr.cond`, `expr.then_branch`, `expr.else_branch`.

This approach avoids repeating the variant names twice on every line.

<div class="example-wrap">

``` rust
// Repetitive; recommend not doing this.
match expr {
    Expr::MethodCall(ExprMethodCall { method, args, .. }) => {
```

</div>

In general, the name to which a syntax tree enum variant is bound should
be a suitable name for the complete syntax tree enum type.

<div class="example-wrap">

``` rust
// Binding is called `base` which is the name I would use if I were
// assigning `*discriminant.base` without an `if let`.
if let Expr::Tuple(base) = *discriminant.base {
```

</div>

A sign that you may not be choosing the right variable names is if you
see names getting repeated in your code, like accessing
`receiver.receiver` or `pat.pat` or `cond.cond`.

</div>

## Variants (Non-exhaustive)<a href="#variants" class="anchor">§</a>

This enum is marked as non-exhaustive

<div class="docblock">

Non-exhaustive enums could have additional variants added in future.
Therefore, when matching against variants of non-exhaustive enums, an
extra wildcard arm must be added to account for any future variants.

</div>

<div class="variants">

<div id="variant.Array" class="section variant">

<a href="#variant.Array" class="anchor">§</a>

### Array(<a href="struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>)

</div>

<div class="docblock">

A slice literal expression: `[a, b, c, d]`.

</div>

<div id="variant.Assign" class="section variant">

<a href="#variant.Assign" class="anchor">§</a>

### Assign(<a href="struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>)

</div>

<div class="docblock">

An assignment expression: `a = compute()`.

</div>

<div id="variant.Async" class="section variant">

<a href="#variant.Async" class="anchor">§</a>

### Async(<a href="struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>)

</div>

<div class="docblock">

An async block: `async { ... }`.

</div>

<div id="variant.Await" class="section variant">

<a href="#variant.Await" class="anchor">§</a>

### Await(<a href="struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>)

</div>

<div class="docblock">

An await expression: `fut.await`.

</div>

<div id="variant.Binary" class="section variant">

<a href="#variant.Binary" class="anchor">§</a>

### Binary(<a href="struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>)

</div>

<div class="docblock">

A binary operation: `a + b`, `a += b`.

</div>

<div id="variant.Block" class="section variant">

<a href="#variant.Block" class="anchor">§</a>

### Block(<a href="struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>)

</div>

<div class="docblock">

A blocked scope: `{ ... }`.

</div>

<div id="variant.Break" class="section variant">

<a href="#variant.Break" class="anchor">§</a>

### Break(<a href="struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>)

</div>

<div class="docblock">

A `break`, with an optional label to break and an optional expression.

</div>

<div id="variant.Call" class="section variant">

<a href="#variant.Call" class="anchor">§</a>

### Call(<a href="struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>)

</div>

<div class="docblock">

A function call expression: `invoke(a, b)`.

</div>

<div id="variant.Cast" class="section variant">

<a href="#variant.Cast" class="anchor">§</a>

### Cast(<a href="struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>)

</div>

<div class="docblock">

A cast expression: `foo as f64`.

</div>

<div id="variant.Closure" class="section variant">

<a href="#variant.Closure" class="anchor">§</a>

### Closure(<a href="struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>)

</div>

<div class="docblock">

A closure expression: `|a, b| a + b`.

</div>

<div id="variant.Const" class="section variant">

<a href="#variant.Const" class="anchor">§</a>

### Const(<a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>)

</div>

<div class="docblock">

A const block: `const { ... }`.

</div>

<div id="variant.Continue" class="section variant">

<a href="#variant.Continue" class="anchor">§</a>

### Continue(<a href="struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>)

</div>

<div class="docblock">

A `continue`, with an optional label.

</div>

<div id="variant.Field" class="section variant">

<a href="#variant.Field" class="anchor">§</a>

### Field(<a href="struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>)

</div>

<div class="docblock">

Access of a named struct field (`obj.k`) or unnamed tuple struct field
(`obj.0`).

</div>

<div id="variant.ForLoop" class="section variant">

<a href="#variant.ForLoop" class="anchor">§</a>

### ForLoop(<a href="struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>)

</div>

<div class="docblock">

A for loop: `for pat in expr { ... }`.

</div>

<div id="variant.Group" class="section variant">

<a href="#variant.Group" class="anchor">§</a>

### Group(<a href="struct.ExprGroup.html" class="struct"
title="struct syn::ExprGroup">ExprGroup</a>)

</div>

<div class="docblock">

An expression contained within invisible delimiters.

This variant is important for faithfully representing the precedence of
expressions and is related to `None`-delimited spans in a `TokenStream`.

</div>

<div id="variant.If" class="section variant">

<a href="#variant.If" class="anchor">§</a>

### If(<a href="struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>)

</div>

<div class="docblock">

An `if` expression with an optional `else` block:
`if expr { ... } else { ... }`.

The `else` branch expression may only be an `If` or `Block` expression,
not any of the other types of expression.

</div>

<div id="variant.Index" class="section variant">

<a href="#variant.Index" class="anchor">§</a>

### Index(<a href="struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>)

</div>

<div class="docblock">

A square bracketed indexing expression: `vector[2]`.

</div>

<div id="variant.Infer" class="section variant">

<a href="#variant.Infer" class="anchor">§</a>

### Infer(<a href="struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>)

</div>

<div class="docblock">

The inferred value of a const generic argument, denoted `_`.

</div>

<div id="variant.Let" class="section variant">

<a href="#variant.Let" class="anchor">§</a>

### Let(<a href="struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>)

</div>

<div class="docblock">

A `let` guard: `let Some(x) = opt`.

</div>

<div id="variant.Lit" class="section variant">

<a href="#variant.Lit" class="anchor">§</a>

### Lit(<a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>)

</div>

<div class="docblock">

A literal in place of an expression: `1`, `"foo"`.

</div>

<div id="variant.Loop" class="section variant">

<a href="#variant.Loop" class="anchor">§</a>

### Loop(<a href="struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>)

</div>

<div class="docblock">

Conditionless loop: `loop { ... }`.

</div>

<div id="variant.Macro" class="section variant">

<a href="#variant.Macro" class="anchor">§</a>

### Macro(<a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>)

</div>

<div class="docblock">

A macro invocation expression: `format!("{}", q)`.

</div>

<div id="variant.Match" class="section variant">

<a href="#variant.Match" class="anchor">§</a>

### Match(<a href="struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>)

</div>

<div class="docblock">

A `match` expression: `match n { Some(n) => {}, None => {} }`.

</div>

<div id="variant.MethodCall" class="section variant">

<a href="#variant.MethodCall" class="anchor">§</a>

### MethodCall(<a href="struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>)

</div>

<div class="docblock">

A method call expression: `x.foo::<T>(a, b)`.

</div>

<div id="variant.Paren" class="section variant">

<a href="#variant.Paren" class="anchor">§</a>

### Paren(<a href="struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>)

</div>

<div class="docblock">

A parenthesized expression: `(a + b)`.

</div>

<div id="variant.Path" class="section variant">

<a href="#variant.Path" class="anchor">§</a>

### Path(<a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>)

</div>

<div class="docblock">

A path like `core::mem::replace` possibly containing generic parameters
and a qualified self-type.

A plain identifier like `x` is a path of length 1.

</div>

<div id="variant.Range" class="section variant">

<a href="#variant.Range" class="anchor">§</a>

### Range(<a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>)

</div>

<div class="docblock">

A range expression: `1..2`, `1..`, `..2`, `1..=2`, `..=2`.

</div>

<div id="variant.RawAddr" class="section variant">

<a href="#variant.RawAddr" class="anchor">§</a>

### RawAddr(<a href="struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>)

</div>

<div class="docblock">

Address-of operation: `&raw const place` or `&raw mut place`.

</div>

<div id="variant.Reference" class="section variant">

<a href="#variant.Reference" class="anchor">§</a>

### Reference(<a href="struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>)

</div>

<div class="docblock">

A referencing operation: `&a` or `&mut a`.

</div>

<div id="variant.Repeat" class="section variant">

<a href="#variant.Repeat" class="anchor">§</a>

### Repeat(<a href="struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>)

</div>

<div class="docblock">

An array literal constructed from one repeated element: `[0u8; N]`.

</div>

<div id="variant.Return" class="section variant">

<a href="#variant.Return" class="anchor">§</a>

### Return(<a href="struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>)

</div>

<div class="docblock">

A `return`, with an optional value to be returned.

</div>

<div id="variant.Struct" class="section variant">

<a href="#variant.Struct" class="anchor">§</a>

### Struct(<a href="struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>)

</div>

<div class="docblock">

A struct literal expression: `Point { x: 1, y: 1 }`.

The `rest` provides the value of the remaining fields as in
`S { a: 1, b: 1, ..rest }`.

</div>

<div id="variant.Try" class="section variant">

<a href="#variant.Try" class="anchor">§</a>

### Try(<a href="struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>)

</div>

<div class="docblock">

A try-expression: `expr?`.

</div>

<div id="variant.TryBlock" class="section variant">

<a href="#variant.TryBlock" class="anchor">§</a>

### TryBlock(<a href="struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>)

</div>

<div class="docblock">

A try block: `try { ... }`.

</div>

<div id="variant.Tuple" class="section variant">

<a href="#variant.Tuple" class="anchor">§</a>

### Tuple(<a href="struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>)

</div>

<div class="docblock">

A tuple expression: `(a, b, c, d)`.

</div>

<div id="variant.Unary" class="section variant">

<a href="#variant.Unary" class="anchor">§</a>

### Unary(<a href="struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>)

</div>

<div class="docblock">

A unary operation: `!x`, `*x`.

</div>

<div id="variant.Unsafe" class="section variant">

<a href="#variant.Unsafe" class="anchor">§</a>

### Unsafe(<a href="struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>)

</div>

<div class="docblock">

An unsafe block: `unsafe { ... }`.

</div>

<div id="variant.Verbatim" class="section variant">

<a href="#variant.Verbatim" class="anchor">§</a>

### Verbatim(<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Tokens in expression position not interpreted by Syn.

</div>

<div id="variant.While" class="section variant">

<a href="#variant.While" class="anchor">§</a>

### While(<a href="struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>)

</div>

<div class="docblock">

A while loop: `while expr { ... }`.

</div>

<div id="variant.Yield" class="section variant">

<a href="#variant.Yield" class="anchor">§</a>

### Yield(<a href="struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>)

</div>

<div class="docblock">

A yield expression: `yield expr`.

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#718-971"
class="src rightside">Source</a><a href="#impl-Expr" class="anchor">§</a>

### impl <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="associatedconstant.PLACEHOLDER"
class="section associatedconstant">

<a href="../src/syn/expr.rs.html#738-745"
class="src rightside">Source</a>

#### pub const <a href="#associatedconstant.PLACEHOLDER"
class="constant">PLACEHOLDER</a>: Self

</div>

<div class="docblock">

An unspecified invalid expression.

<div class="example-wrap">

``` rust
use core::mem;
use quote::ToTokens;
use syn::{parse_quote, Expr};

fn unparenthesize(e: &mut Expr) {
    while let Expr::Paren(paren) = e {
        *e = mem::replace(&mut *paren.expr, Expr::PLACEHOLDER);
    }
}

fn main() {
    let mut e: Expr = parse_quote! { ((1 + 1)) };
    unparenthesize(&mut e);
    assert_eq!("1 + 1", e.to_token_stream().to_string());
}
```

</div>

</div>

<div id="method.parse_without_eager_brace" class="section method">

<a href="../src/syn/expr.rs.html#830-832"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_without_eager_brace"
class="fn">parse_without_eager_brace</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>\>

</div>

<div class="docblock">

An alternative to the primary `Expr::parse` parser (from the
[`Parse`](parse/trait.Parse.html "trait syn::parse::Parse") trait) for
ambiguous syntactic positions in which a trailing brace should not be
taken as part of the expression.

Rust grammar has an ambiguity where braces sometimes turn a path
expression into a struct initialization and sometimes do not. In the
following code, the expression `S {}` is one expression. Presumably
there is an empty struct `struct S {}` defined somewhere which it is
instantiating.

<div class="example-wrap">

``` rust
let _ = *S {};

// parsed by rustc as: `*(S {})`
```

</div>

We would want to parse the above using `Expr::parse` after the `=`
token.

But in the following, `S {}` is *not* a struct init expression.

<div class="example-wrap">

``` rust
if *S {} {}

// parsed by rustc as:
//
//    if (*S) {
//        /* empty block */
//    }
//    {
//        /* another empty block */
//    }
```

</div>

For that reason we would want to parse if-conditions using
`Expr::parse_without_eager_brace` after the `if` token. Same for similar
syntactic positions such as the condition expr after a `while` token or
the expr at the top of a `match`.

The Rust grammar’s choices around which way this ambiguity is resolved
at various syntactic positions is fairly arbitrary. Really either parse
behavior could work in most positions, and language designers just
decide each case based on which is more likely to be what the programmer
had in mind most of the time.

<div class="example-wrap">

``` rust
if return S {} {}

// parsed by rustc as:
//
//    if (return (S {})) {
//    }
//
// but could equally well have been this other arbitrary choice:
//
//    if (return S) {
//    }
//    {}
```

</div>

Note the grammar ambiguity on trailing braces is distinct from
precedence and is not captured by assigning a precedence level to the
braced struct init expr in relation to other operators. This can be
illustrated by `return 0..S {}` vs `match 0..S {}`. The former parses as
`return (0..(S {}))` implying tighter precedence for struct init than
`..`, while the latter parses as `match (0..S) {}` implying tighter
precedence for `..` than struct init, a contradiction.

</div>

<div id="method.parse_with_earlier_boundary_rule"
class="section method">

<a href="../src/syn/expr.rs.html#892-894"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_with_earlier_boundary_rule"
class="fn">parse_with_earlier_boundary_rule</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>\>

</div>

<div class="docblock">

An alternative to the primary `Expr::parse` parser (from the
[`Parse`](parse/trait.Parse.html "trait syn::parse::Parse") trait) for
syntactic positions in which expression boundaries are placed more
eagerly than done by the typical expression grammar. This includes
expressions at the head of a statement or in the right-hand side of a
`match` arm.

Compare the following cases:

1.  

<div class="example-wrap">

``` rust
let _ = match result {
    () if guard => if cond { f } else { g }
    () => false,
};
```

</div>

2.  

<div class="example-wrap">

``` rust
let _ = || {
    if cond { f } else { g }
    ()
};
```

</div>

3.  

<div class="example-wrap">

``` rust
let _ = [if cond { f } else { g } ()];
```

</div>

The same sequence of tokens `if cond { f } else { g } ()` appears in
expression position 3 times. The first two syntactic positions use eager
placement of expression boundaries, and parse as `Expr::If`, with the
adjacent `()` becoming `Pat::Tuple` or `Expr::Tuple`. In contrast, the
third case uses standard expression boundaries and parses as
`Expr::Call`.

As with
[`parse_without_eager_brace`](enum.Expr.html#method.parse_without_eager_brace "associated function syn::Expr::parse_without_eager_brace"),
this ambiguity in the Rust grammar is independent of precedence.

</div>

<div id="method.peek" class="section method">

<a href="../src/syn/expr.rs.html#908-924"
class="src rightside">Source</a>

#### pub fn <a href="#method.peek" class="fn">peek</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns whether the next token in the parse stream is one that might
possibly form the beginning of an expr.

This classification is a load-bearing part of the grammar of some Rust
expressions, notably `return` and `break`. For example `return < …` will
never parse `<` as a binary operator regardless of what comes after,
because `<` is a legal starting token for an expression and so it’s
required to be continued as a return value, such as
`return <Struct as Trait>::CONST`. Meanwhile `return > …` treats the `>`
as a binary operator because it cannot be a starting token for any Rust
expression.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Expr" class="section impl">

<a href="../src/syn/gen/clone.rs.html#239-310"
class="src rightside">Source</a><a href="#impl-Clone-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/syn/gen/clone.rs.html#240-309"
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

<div id="impl-Debug-for-Expr" class="section impl">

<a href="../src/syn/gen/debug.rs.html#416-492"
class="src rightside">Source</a><a href="#impl-Debug-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/syn/gen/debug.rs.html#417-491"
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

<div id="impl-From%3CExprArray%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprArray%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprAssign%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprAssign%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-1" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprAsync%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprAsync%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-2" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprAwait%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprAwait%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-3" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-3" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprBinary%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprBinary%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-4" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-4" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprBlock%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprBlock%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-5" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-5" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprBreak%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprBreak%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-6" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-6" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprCall%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprCall%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-7" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-7" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprCast%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprCast%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-8" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-8" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprClosure%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprClosure%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-9" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-9" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprConst%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprConst%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-10" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-10" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprContinue%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprContinue%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-11" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-11" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprField%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprField%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-12" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-12" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprForLoop%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprForLoop%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-13" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-13" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprGroup%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprGroup%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprGroup.html" class="struct"
title="struct syn::ExprGroup">ExprGroup</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-14" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-14" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprGroup.html" class="struct"
title="struct syn::ExprGroup">ExprGroup</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprIf%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprIf%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-15" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-15" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprIndex%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprIndex%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-16" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-16" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprInfer%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprInfer%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-17" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-17" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprLet%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprLet%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-18" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-18" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprLit%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprLit%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-19" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-19" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprLoop%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprLoop%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-20" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-20" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprMacro%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprMacro%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-21" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-21" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprMatch%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprMatch%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-22" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-22" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprMethodCall%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprMethodCall%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-23" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-23" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprParen%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprParen%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-24" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-24" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprPath%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprPath%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-25" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-25" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprRange%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprRange%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-26" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-26" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprRawAddr%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprRawAddr%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-27" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-27" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprReference%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprReference%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-28" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-28" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprRepeat%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprRepeat%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-29" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-29" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprReturn%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprReturn%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-30" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-30" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprStruct%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprStruct%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-31" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-31" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprTry%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprTry%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-32" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-32" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprTryBlock%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprTryBlock%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-33" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-33" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprTuple%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprTuple%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-34" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-34" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprUnary%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprUnary%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-35" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-35" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprUnsafe%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprUnsafe%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-36" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-36" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprWhile%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprWhile%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-37" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-37" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExprYield%3E-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-From%3CExprYield%3E-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>\> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.from-38" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.from-38" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(e: <a href="struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>) -\> <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-Hash-for-Expr" class="section impl">

<a href="../src/syn/gen/hash.rs.html#350-544"
class="src rightside">Source</a><a href="#impl-Hash-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/syn/gen/hash.rs.html#351-543"
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

<div id="impl-Parse-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#1234-1242"
class="src rightside">Source</a><a href="#impl-Parse-for-Expr" class="anchor">§</a>

### impl <a href="parse/trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.parse" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#1235-1241"
class="src rightside">Source</a><a href="#method.parse" class="anchor">§</a>

#### fn <a href="parse/trait.Parse.html#tymethod.parse" class="fn">parse</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-PartialEq-for-Expr" class="section impl">

<a href="../src/syn/gen/eq.rs.html#267-353"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/syn/gen/eq.rs.html#268-352"
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

<div id="impl-ToTokens-for-Expr" class="section impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Expr" class="anchor">§</a>

### impl <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/syn/expr.rs.html#37-269"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

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

<div id="impl-Eq-for-Expr" class="section impl">

<a href="../src/syn/gen/eq.rs.html#264" class="src rightside">Source</a><a href="#impl-Eq-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Expr" class="section impl">

<a href="#impl-Freeze-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-RefUnwindSafe-for-Expr" class="section impl">

<a href="#impl-RefUnwindSafe-for-Expr" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-Send-for-Expr" class="section impl">

<a href="#impl-Send-for-Expr" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-Sync-for-Expr" class="section impl">

<a href="#impl-Sync-for-Expr" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-Unpin-for-Expr" class="section impl">

<a href="#impl-Unpin-for-Expr" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-UnwindSafe-for-Expr" class="section impl">

<a href="#impl-UnwindSafe-for-Expr" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

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

<div id="method.from-39" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-39" class="anchor">§</a>

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
