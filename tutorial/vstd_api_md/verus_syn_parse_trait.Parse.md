<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[parse](index.html)

</div>

# Trait <span class="trait">Parse</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/parse.rs.html#214-216"
class="src">Source</a> </span>

</div>

``` rust
pub trait Parse: Sized {
    // Required method
    fn parse(input: ParseStream<'_>) -> Result<Self>;
}
```

Expand description

<div class="docblock">

Parsing interface implemented by all types that can be parsed in a
default way from a token stream.

Refer to the [module documentation](index.html "mod verus_syn::parse")
for details about implementing and using the `Parse` trait.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.parse" class="section method">

<a href="../../src/verus_syn/parse.rs.html#215"
class="src rightside">Source</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-Parse-for-TokenTree" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1206-1213"
class="src rightside">Source</a><a href="#impl-Parse-for-TokenTree" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>

</div>

<div class="impl-items">

<div id="method.parse" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1207-1212"
class="src rightside">Source</a><a href="#method.parse" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CAbi%3E" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#1145-1153"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CAbi%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Abi.html" class="struct"
title="struct verus_syn::Abi">Abi</a>\>

</div>

<div class="impl-items">

<div id="method.parse-1" class="section method trait-impl">

<a href="../../src/verus_syn/ty.rs.html#1146-1152"
class="src rightside">Source</a><a href="#method.parse-1" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CBoundLifetimes%3E"
class="section impl">

<a href="../../src/verus_syn/generics.rs.html#688-696"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CBoundLifetimes%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.BoundLifetimes.html" class="struct"
title="struct verus_syn::BoundLifetimes">BoundLifetimes</a>\>

</div>

<div class="impl-items">

<div id="method.parse-2" class="section method trait-impl">

<a href="../../src/verus_syn/generics.rs.html#689-695"
class="src rightside">Source</a><a href="#method.parse-2" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CDecreases%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1086-1094"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CDecreases%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Decreases.html" class="struct"
title="struct verus_syn::Decreases">Decreases</a>\>

</div>

<div class="impl-items">

<div id="method.parse-3" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1087-1093"
class="src rightside">Source</a><a href="#method.parse-3" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CDefaultEnsures%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1031-1039"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CDefaultEnsures%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::DefaultEnsures">DefaultEnsures</a>\>

</div>

<div class="impl-items">

<div id="method.parse-4" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1032-1038"
class="src rightside">Source</a><a href="#method.parse-4" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CEnsures%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1020-1028"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CEnsures%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Ensures.html" class="struct"
title="struct verus_syn::Ensures">Ensures</a>\>

</div>

<div class="impl-items">

<div id="method.parse-5" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1021-1027"
class="src rightside">Source</a><a href="#method.parse-5" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CFnProofOptions%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1579-1587"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CFnProofOptions%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.FnProofOptions.html" class="struct"
title="struct verus_syn::FnProofOptions">FnProofOptions</a>\>

</div>

<div class="impl-items">

<div id="method.parse-6" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1580-1586"
class="src rightside">Source</a><a href="#method.parse-6" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CInvariant%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1064-1072"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CInvariant%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Invariant.html" class="struct"
title="struct verus_syn::Invariant">Invariant</a>\>

</div>

<div class="impl-items">

<div id="method.parse-7" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1065-1071"
class="src rightside">Source</a><a href="#method.parse-7" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CInvariantEnsures%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1075-1083"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CInvariantEnsures%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::InvariantEnsures">InvariantEnsures</a>\>

</div>

<div class="impl-items">

<div id="method.parse-8" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1076-1082"
class="src rightside">Source</a><a href="#method.parse-8" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CInvariantExceptBreak%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1053-1061"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CInvariantExceptBreak%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::InvariantExceptBreak">InvariantExceptBreak</a>\>

</div>

<div class="impl-items">

<div id="method.parse-9" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1054-1060"
class="src rightside">Source</a><a href="#method.parse-9" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CLabel%3E" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2977-2985"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CLabel%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Label.html" class="struct"
title="struct verus_syn::Label">Label</a>\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.parse-10" class="section method trait-impl">

<a href="../../src/verus_syn/expr.rs.html#2978-2984"
class="src rightside">Source</a><a href="#method.parse-10" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CProver%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#987-995"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CProver%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Prover.html" class="struct"
title="struct verus_syn::Prover">Prover</a>\>

</div>

<div class="impl-items">

<div id="method.parse-11" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#988-994"
class="src rightside">Source</a><a href="#method.parse-11" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CRecommends%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1009-1017"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CRecommends%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Recommends.html" class="struct"
title="struct verus_syn::Recommends">Recommends</a>\>

</div>

<div class="impl-items">

<div id="method.parse-12" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1010-1016"
class="src rightside">Source</a><a href="#method.parse-12" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CRequires%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#998-1006"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CRequires%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Requires.html" class="struct"
title="struct verus_syn::Requires">Requires</a>\>

</div>

<div class="impl-items">

<div id="method.parse-13" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#999-1005"
class="src rightside">Source</a><a href="#method.parse-13" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CReturns%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1042-1050"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CReturns%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Returns.html" class="struct"
title="struct verus_syn::Returns">Returns</a>\>

</div>

<div class="impl-items">

<div id="method.parse-14" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1043-1049"
class="src rightside">Source</a><a href="#method.parse-14" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CSignatureDecreases%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1097-1105"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CSignatureDecreases%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.SignatureDecreases.html" class="struct"
title="struct verus_syn::SignatureDecreases">SignatureDecreases</a>\>

</div>

<div class="impl-items">

<div id="method.parse-15" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1098-1104"
class="src rightside">Source</a><a href="#method.parse-15" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CSignatureInvariants%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#919-927"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CSignatureInvariants%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.SignatureInvariants.html" class="struct"
title="struct verus_syn::SignatureInvariants">SignatureInvariants</a>\>

</div>

<div class="impl-items">

<div id="method.parse-16" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#920-926"
class="src rightside">Source</a><a href="#method.parse-16" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CSignatureUnwind%3E"
class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1108-1116"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CSignatureUnwind%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.SignatureUnwind.html" class="struct"
title="struct verus_syn::SignatureUnwind">SignatureUnwind</a>\>

</div>

<div class="impl-items">

<div id="method.parse-17" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#1109-1115"
class="src rightside">Source</a><a href="#method.parse-17" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CWhereClause%3E" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#975-983"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CWhereClause%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.WhereClause.html" class="struct"
title="struct verus_syn::WhereClause">WhereClause</a>\>

</div>

<div class="impl-items">

<div id="method.parse-18" class="section method trait-impl">

<a href="../../src/verus_syn/generics.rs.html#976-982"
class="src rightside">Source</a><a href="#method.parse-18" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CWithSpecOnFn%3E" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#2430-2438"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CWithSpecOnFn%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.WithSpecOnFn.html" class="struct"
title="struct verus_syn::WithSpecOnFn">WithSpecOnFn</a>\>

</div>

<div class="impl-items">

<div id="method.parse-19" class="section method trait-impl">

<a href="../../src/verus_syn/verus.rs.html#2431-2437"
class="src rightside">Source</a><a href="#method.parse-19" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Group" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1216-1227"
class="src rightside">Source</a><a href="#impl-Parse-for-Group" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Group.html" class="struct"
title="struct proc_macro2::Group">Group</a>

</div>

<div class="impl-items">

<div id="method.parse-20" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1217-1226"
class="src rightside">Source</a><a href="#method.parse-20" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Literal" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1240-1247"
class="src rightside">Source</a><a href="#impl-Parse-for-Literal" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.parse-21" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1241-1246"
class="src rightside">Source</a><a href="#method.parse-21" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Punct" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1230-1237"
class="src rightside">Source</a><a href="#impl-Parse-for-Punct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Punct.html" class="struct"
title="struct proc_macro2::Punct">Punct</a>

</div>

<div class="impl-items">

<div id="method.parse-22" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1231-1236"
class="src rightside">Source</a><a href="#method.parse-22" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-TokenStream" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1199-1203"
class="src rightside">Source</a><a href="#impl-Parse-for-TokenStream" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.parse-23" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1200-1202"
class="src rightside">Source</a><a href="#method.parse-23" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CT%3E" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1188-1196"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> + <a href="../token/trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a>\> <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.parse-24" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1189-1195"
class="src rightside">Source</a><a href="#method.parse-24" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Box%3CT%3E" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1181-1185"
class="src rightside">Source</a><a href="#impl-Parse-for-Box%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>\> <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/boxed/struct.Box.html"
class="struct" title="struct alloc::boxed::Box">Box</a>\<T\>

</div>

<div class="impl-items">

<div id="method.parse-25" class="section method trait-impl">

<a href="../../src/verus_syn/parse.rs.html#1182-1184"
class="src rightside">Source</a><a href="#method.parse-25" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Parse-for-BinOp" class="section impl">

<a href="../../src/verus_syn/op.rs.html#103-183"
class="src rightside">Source</a><a href="#impl-Parse-for-BinOp" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-Parse-for-CapturedParam" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#1094-1105"
class="src rightside">Source</a><a href="#impl-Parse-for-CapturedParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.CapturedParam.html" class="enum"
title="enum verus_syn::CapturedParam">CapturedParam</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-DataMode" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#637-652"
class="src rightside">Source</a><a href="#impl-Parse-for-DataMode" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.DataMode.html" class="enum"
title="enum verus_syn::DataMode">DataMode</a>

</div>

<div id="impl-Parse-for-Expr" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#1283-1291"
class="src rightside">Source</a><a href="#impl-Parse-for-Expr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Expr.html" class="enum"
title="enum verus_syn::Expr">Expr</a>

</div>

<div id="impl-Parse-for-FnMode" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#655-690"
class="src rightside">Source</a><a href="#impl-Parse-for-FnMode" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.FnMode.html" class="enum"
title="enum verus_syn::FnMode">FnMode</a>

</div>

<div id="impl-Parse-for-ForeignItem" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2022-2118"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.ForeignItem.html" class="enum"
title="enum verus_syn::ForeignItem">ForeignItem</a>

</div>

<div id="impl-Parse-for-GenericArgument" class="section impl">

<a href="../../src/verus_syn/path.rs.html#316-407"
class="src rightside">Source</a><a href="#impl-Parse-for-GenericArgument" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.GenericArgument.html" class="enum"
title="enum verus_syn::GenericArgument">GenericArgument</a>

</div>

<div id="impl-Parse-for-GenericParam" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#601-625"
class="src rightside">Source</a><a href="#impl-Parse-for-GenericParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.GenericParam.html" class="enum"
title="enum verus_syn::GenericParam">GenericParam</a>

</div>

<div id="impl-Parse-for-GlobalInner" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1553-1563"
class="src rightside">Source</a><a href="#impl-Parse-for-GlobalInner" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.GlobalInner.html" class="enum"
title="enum verus_syn::GlobalInner">GlobalInner</a>

</div>

<div id="impl-Parse-for-ImplItem" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2861-2974"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.ImplItem.html" class="enum"
title="enum verus_syn::ImplItem">ImplItem</a>

</div>

<div id="impl-Parse-for-InvariantNameSet" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#930-947"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantNameSet" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.InvariantNameSet.html" class="enum"
title="enum verus_syn::InvariantNameSet">InvariantNameSet</a>

</div>

<div id="impl-Parse-for-Item" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1008-1014"
class="src rightside">Source</a><a href="#impl-Parse-for-Item" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Item.html" class="enum"
title="enum verus_syn::Item">Item</a>

</div>

<div id="impl-Parse-for-Lit" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#873-902"
class="src rightside">Source</a><a href="#impl-Parse-for-Lit" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Lit.html" class="enum"
title="enum verus_syn::Lit">Lit</a>

</div>

<div id="impl-Parse-for-Member" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3257-3267"
class="src rightside">Source</a><a href="#impl-Parse-for-Member" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>

</div>

<div id="impl-Parse-for-Meta" class="section impl">

<a href="../../src/verus_syn/attr.rs.html#687-692"
class="src rightside">Source</a><a href="#impl-Parse-for-Meta" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Meta.html" class="enum"
title="enum verus_syn::Meta">Meta</a>

</div>

<div id="impl-Parse-for-Mode" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#619-634"
class="src rightside">Source</a><a href="#impl-Parse-for-Mode" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Mode.html" class="enum"
title="enum verus_syn::Mode">Mode</a>

</div>

<div id="impl-Parse-for-PointerMutability" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3368-3379"
class="src rightside">Source</a><a href="#impl-Parse-for-PointerMutability" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.PointerMutability.html" class="enum"
title="enum verus_syn::PointerMutability">PointerMutability</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Publish" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#592-616"
class="src rightside">Source</a><a href="#impl-Parse-for-Publish" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Publish.html" class="enum"
title="enum verus_syn::Publish">Publish</a>

</div>

<div id="impl-Parse-for-RangeLimits" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3205-3219"
class="src rightside">Source</a><a href="#impl-Parse-for-RangeLimits" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.RangeLimits.html" class="enum"
title="enum verus_syn::RangeLimits">RangeLimits</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ReturnType" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#894-899"
class="src rightside">Source</a><a href="#impl-Parse-for-ReturnType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.ReturnType.html" class="enum"
title="enum verus_syn::ReturnType">ReturnType</a>

</div>

<div id="impl-Parse-for-StaticMutability" class="section impl">

<a href="../../src/verus_syn/item.rs.html#3162-3167"
class="src rightside">Source</a><a href="#impl-Parse-for-StaticMutability" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.StaticMutability.html" class="enum"
title="enum verus_syn::StaticMutability">StaticMutability</a>

</div>

<div id="impl-Parse-for-Stmt" class="section impl">

<a href="../../src/verus_syn/stmt.rs.html#193-198"
class="src rightside">Source</a><a href="#impl-Parse-for-Stmt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Stmt.html" class="enum"
title="enum verus_syn::Stmt">Stmt</a>

</div>

<div id="impl-Parse-for-TraitBoundModifier" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#892-900"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitBoundModifier" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum verus_syn::TraitBoundModifier">TraitBoundModifier</a>

</div>

<div id="impl-Parse-for-TraitItem" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2522-2609"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.TraitItem.html" class="enum"
title="enum verus_syn::TraitItem">TraitItem</a>

</div>

<div id="impl-Parse-for-Type" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#302-308"
class="src rightside">Source</a><a href="#impl-Parse-for-Type" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../enum.Type.html" class="enum"
title="enum verus_syn::Type">Type</a>

</div>

<div id="impl-Parse-for-TypeParamBound" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#743-749"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParamBound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.TypeParamBound.html" class="enum"
title="enum verus_syn::TypeParamBound">TypeParamBound</a>

</div>

<div id="impl-Parse-for-UnOp" class="section impl">

<a href="../../src/verus_syn/op.rs.html#186-207"
class="src rightside">Source</a><a href="#impl-Parse-for-UnOp" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.UnOp.html" class="enum"
title="enum verus_syn::UnOp">UnOp</a>

</div>

<div id="impl-Parse-for-UseTree" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1466-1471"
class="src rightside">Source</a><a href="#impl-Parse-for-UseTree" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.UseTree.html" class="enum"
title="enum verus_syn::UseTree">UseTree</a>

</div>

<div id="impl-Parse-for-Visibility" class="section impl">

<a href="../../src/verus_syn/restriction.rs.html#71-90"
class="src rightside">Source</a><a href="#impl-Parse-for-Visibility" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.Visibility.html" class="enum"
title="enum verus_syn::Visibility">Visibility</a>

</div>

<div id="impl-Parse-for-WherePredicate" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#986-1052"
class="src rightside">Source</a><a href="#impl-Parse-for-WherePredicate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../enum.WherePredicate.html" class="enum"
title="enum verus_syn::WherePredicate">WherePredicate</a>

</div>

<div id="impl-Parse-for-Abi" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#1135-1142"
class="src rightside">Source</a><a href="#impl-Parse-for-Abi" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Abi.html" class="struct"
title="struct verus_syn::Abi">Abi</a>

</div>

<div id="impl-Parse-for-AngleBracketedGenericArguments"
class="section impl">

<a href="../../src/verus_syn/path.rs.html#488-493"
class="src rightside">Source</a><a href="#impl-Parse-for-AngleBracketedGenericArguments"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct verus_syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>

</div>

<div id="impl-Parse-for-Arm" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3282-3312"
class="src rightside">Source</a><a href="#impl-Parse-for-Arm" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Arm.html" class="struct"
title="struct verus_syn::Arm">Arm</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Assert" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1195-1256"
class="src rightside">Source</a><a href="#impl-Parse-for-Assert" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Assert.html" class="struct"
title="struct verus_syn::Assert">Assert</a>

</div>

<div id="impl-Parse-for-AssertForall" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1259-1310"
class="src rightside">Source</a><a href="#impl-Parse-for-AssertForall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.AssertForall.html" class="struct"
title="struct verus_syn::AssertForall">AssertForall</a>

</div>

<div id="impl-Parse-for-Assume" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1175-1192"
class="src rightside">Source</a><a href="#impl-Parse-for-Assume" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Assume.html" class="struct"
title="struct verus_syn::Assume">Assume</a>

</div>

<div id="impl-Parse-for-AssumeSpecification" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1403-1458"
class="src rightside">Source</a><a href="#impl-Parse-for-AssumeSpecification" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::AssumeSpecification">AssumeSpecification</a>

</div>

<div id="impl-Parse-for-BareFnArg" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#1064-1069"
class="src rightside">Source</a><a href="#impl-Parse-for-BareFnArg" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.BareFnArg.html" class="struct"
title="struct verus_syn::BareFnArg">BareFnArg</a>

</div>

<div id="impl-Parse-for-Block" class="section impl">

<a href="../../src/verus_syn/stmt.rs.html#182-190"
class="src rightside">Source</a><a href="#impl-Parse-for-Block" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Block.html" class="struct"
title="struct verus_syn::Block">Block</a>

</div>

<div id="impl-Parse-for-BoundLifetimes" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#666-685"
class="src rightside">Source</a><a href="#impl-Parse-for-BoundLifetimes" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.BoundLifetimes.html" class="struct"
title="struct verus_syn::BoundLifetimes">BoundLifetimes</a>

</div>

<div id="impl-Parse-for-BroadcastUse" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1359-1400"
class="src rightside">Source</a><a href="#impl-Parse-for-BroadcastUse" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.BroadcastUse.html" class="struct"
title="struct verus_syn::BroadcastUse">BroadcastUse</a>

</div>

<div id="impl-Parse-for-ConstParam" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#903-924"
class="src rightside">Source</a><a href="#impl-Parse-for-ConstParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ConstParam.html" class="struct"
title="struct verus_syn::ConstParam">ConstParam</a>

</div>

<div id="impl-Parse-for-Decreases" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#855-862"
class="src rightside">Source</a><a href="#impl-Parse-for-Decreases" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Decreases.html" class="struct"
title="struct verus_syn::Decreases">Decreases</a>

</div>

<div id="impl-Parse-for-DefaultEnsures" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#803-811"
class="src rightside">Source</a><a href="#impl-Parse-for-DefaultEnsures" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::DefaultEnsures">DefaultEnsures</a>

</div>

<div id="impl-Parse-for-DeriveInput" class="section impl">

<a href="../../src/verus_syn/derive.rs.html#81-151"
class="src rightside">Source</a><a href="#impl-Parse-for-DeriveInput" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.DeriveInput.html" class="struct"
title="struct verus_syn::DeriveInput">DeriveInput</a>

</div>

<div id="impl-Parse-for-Ensures" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#789-800"
class="src rightside">Source</a><a href="#impl-Parse-for-Ensures" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Ensures.html" class="struct"
title="struct verus_syn::Ensures">Ensures</a>

</div>

<div id="impl-Parse-for-ExprArray" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2310-2332"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprArray" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprArray.html" class="struct"
title="struct verus_syn::ExprArray">ExprArray</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAssign" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAssign" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprAssign.html" class="struct"
title="struct verus_syn::ExprAssign">ExprAssign</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAsync" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2856-2865"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAsync" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprAsync.html" class="struct"
title="struct verus_syn::ExprAsync">ExprAsync</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAwait" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAwait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprAwait.html" class="struct"
title="struct verus_syn::ExprAwait">ExprAwait</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBinary" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBinary" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprBinary.html" class="struct"
title="struct verus_syn::ExprBinary">ExprBinary</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBlock" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3137-3153"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBlock" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprBlock.html" class="struct"
title="struct verus_syn::ExprBlock">ExprBlock</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBreak" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2720-2725"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBreak" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprBreak.html" class="struct"
title="struct verus_syn::ExprBreak">ExprBreak</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprCall" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprCall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprCall.html" class="struct"
title="struct verus_syn::ExprCall">ExprCall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprCast" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprCast" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprCast.html" class="struct"
title="struct verus_syn::ExprCast">ExprCast</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprClosure" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2682-2687"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprClosure" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprClosure.html" class="struct"
title="struct verus_syn::ExprClosure">ExprClosure</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprConst" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2947-2962"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprConst.html" class="struct"
title="struct verus_syn::ExprConst">ExprConst</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprContinue" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2989-2997"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprContinue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprContinue.html" class="struct"
title="struct verus_syn::ExprContinue">ExprContinue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprField" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprField" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprField.html" class="struct"
title="struct verus_syn::ExprField">ExprField</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprForLoop" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2521-2558"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprForLoop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprForLoop.html" class="struct"
title="struct verus_syn::ExprForLoop">ExprForLoop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprGetField" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprGetField" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprGetField.html" class="struct"
title="struct verus_syn::ExprGetField">ExprGetField</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprIf" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2456-2506"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprIf" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprIf.html" class="struct"
title="struct verus_syn::ExprIf">ExprIf</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprIndex" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprIndex" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprIndex.html" class="struct"
title="struct verus_syn::ExprIndex">ExprIndex</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprInfer" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2510-2517"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprInfer" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprInfer.html" class="struct"
title="struct verus_syn::ExprInfer">ExprInfer</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprLet" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2433-2438"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLet" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprLet.html" class="struct"
title="struct verus_syn::ExprLet">ExprLet</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprLit" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2375-2382"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLit" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprLit.html" class="struct"
title="struct verus_syn::ExprLit">ExprLit</a>

</div>

<div id="impl-Parse-for-ExprLoop" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2562-2590"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLoop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprLoop.html" class="struct"
title="struct verus_syn::ExprLoop">ExprLoop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprMacro" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2216-2223"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprMacro.html" class="struct"
title="struct verus_syn::ExprMacro">ExprMacro</a>

</div>

<div id="impl-Parse-for-ExprMatch" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2594-2614"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMatch" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprMatch.html" class="struct"
title="struct verus_syn::ExprMatch">ExprMatch</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprMethodCall" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMethodCall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprMethodCall.html" class="struct"
title="struct verus_syn::ExprMethodCall">ExprMethodCall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprParen" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2420-2429"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprParen" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprParen.html" class="struct"
title="struct verus_syn::ExprParen">ExprParen</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprPath" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3242-3254"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprPath" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprPath.html" class="struct"
title="struct verus_syn::ExprPath">ExprPath</a>

</div>

<div id="impl-Parse-for-ExprRange" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRange" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprRange.html" class="struct"
title="struct verus_syn::ExprRange">ExprRange</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprRawAddr" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2691-2702"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRawAddr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprRawAddr.html" class="struct"
title="struct verus_syn::ExprRawAddr">ExprRawAddr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprReference" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2706-2716"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprReference" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprReference.html" class="struct"
title="struct verus_syn::ExprReference">ExprReference</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprRepeat" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2336-2347"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRepeat" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprRepeat.html" class="struct"
title="struct verus_syn::ExprRepeat">ExprRepeat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprReturn" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2729-2743"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprReturn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprReturn.html" class="struct"
title="struct verus_syn::ExprReturn">ExprReturn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprStruct" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3063-3069"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprStruct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprStruct.html" class="struct"
title="struct verus_syn::ExprStruct">ExprStruct</a>

</div>

<div id="impl-Parse-for-ExprTry" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTry" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprTry.html" class="struct"
title="struct verus_syn::ExprTry">ExprTry</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprTryBlock" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2755-2763"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTryBlock" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprTryBlock.html" class="struct"
title="struct verus_syn::ExprTryBlock">ExprTryBlock</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprTuple" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTuple" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprTuple.html" class="struct"
title="struct verus_syn::ExprTuple">ExprTuple</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprUnary" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2659-2665"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprUnary" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprUnary.html" class="struct"
title="struct verus_syn::ExprUnary">ExprUnary</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprUnsafe" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3118-3133"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprUnsafe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprUnsafe.html" class="struct"
title="struct verus_syn::ExprUnsafe">ExprUnsafe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprWhile" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2913-2943"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprWhile" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprWhile.html" class="struct"
title="struct verus_syn::ExprWhile">ExprWhile</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprYield" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2767-2781"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprYield" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ExprYield.html" class="struct"
title="struct verus_syn::ExprYield">ExprYield</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-FieldValue" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3034-3060"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.FieldValue.html" class="struct"
title="struct verus_syn::FieldValue">FieldValue</a>

</div>

<div id="impl-Parse-for-FieldsNamed" class="section impl">

<a href="../../src/verus_syn/data.rs.html#302-310"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldsNamed" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.FieldsNamed.html" class="struct"
title="struct verus_syn::FieldsNamed">FieldsNamed</a>

</div>

<div id="impl-Parse-for-FieldsUnnamed" class="section impl">

<a href="../../src/verus_syn/data.rs.html#313-321"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldsUnnamed" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct verus_syn::FieldsUnnamed">FieldsUnnamed</a>

</div>

<div id="impl-Parse-for-File" class="section impl">

<a href="../../src/verus_syn/file.rs.html#94-108"
class="src rightside">Source</a><a href="#impl-Parse-for-File" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.File.html" class="struct"
title="struct verus_syn::File">File</a>

</div>

<div id="impl-Parse-for-FnArg" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1758-1767"
class="src rightside">Source</a><a href="#impl-Parse-for-FnArg" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.FnArg.html" class="struct"
title="struct verus_syn::FnArg">FnArg</a>

</div>

<div id="impl-Parse-for-FnProofOptions" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1566-1576"
class="src rightside">Source</a><a href="#impl-Parse-for-FnProofOptions" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.FnProofOptions.html" class="struct"
title="struct verus_syn::FnProofOptions">FnProofOptions</a>

</div>

<div id="impl-Parse-for-ForeignItemFn" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2121-2134"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemFn.html" class="struct"
title="struct verus_syn::ForeignItemFn">ForeignItemFn</a>

</div>

<div id="impl-Parse-for-ForeignItemMacro" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2202-2217"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct verus_syn::ForeignItemMacro">ForeignItemMacro</a>

</div>

<div id="impl-Parse-for-ForeignItemStatic" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2137-2150"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemStatic" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct verus_syn::ForeignItemStatic">ForeignItemStatic</a>

</div>

<div id="impl-Parse-for-ForeignItemType" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2153-2168"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemType.html" class="struct"
title="struct verus_syn::ForeignItemType">ForeignItemType</a>

</div>

<div id="impl-Parse-for-Generics" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#538-598"
class="src rightside">Source</a><a href="#impl-Parse-for-Generics" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Generics.html" class="struct"
title="struct verus_syn::Generics">Generics</a>

</div>

<div id="impl-Parse-for-Global" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1484-1498"
class="src rightside">Source</a><a href="#impl-Parse-for-Global" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Global.html" class="struct"
title="struct verus_syn::Global">Global</a>

</div>

<div id="impl-Parse-for-GlobalLayout" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1518-1550"
class="src rightside">Source</a><a href="#impl-Parse-for-GlobalLayout" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.GlobalLayout.html" class="struct"
title="struct verus_syn::GlobalLayout">GlobalLayout</a>

</div>

<div id="impl-Parse-for-GlobalSizeOf" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1501-1515"
class="src rightside">Source</a><a href="#impl-Parse-for-GlobalSizeOf" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.GlobalSizeOf.html" class="struct"
title="struct verus_syn::GlobalSizeOf">GlobalSizeOf</a>

</div>

<div id="impl-Parse-for-Ident" class="section impl">

<a href="../../src/verus_syn/ident.rs.html#76-93"
class="src rightside">Source</a><a href="#impl-Parse-for-Ident" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Parse-for-ImplItemConst" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2977-3025"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemConst.html" class="struct"
title="struct verus_syn::ImplItemConst">ImplItemConst</a>

</div>

<div id="impl-Parse-for-ImplItemFn" class="section impl">

<a href="../../src/verus_syn/item.rs.html#3028-3032"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemFn.html" class="struct"
title="struct verus_syn::ImplItemFn">ImplItemFn</a>

</div>

<div id="impl-Parse-for-ImplItemMacro" class="section impl">

<a href="../../src/verus_syn/item.rs.html#3135-3150"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemMacro.html" class="struct"
title="struct verus_syn::ImplItemMacro">ImplItemMacro</a>

</div>

<div id="impl-Parse-for-ImplItemType" class="section impl">

<a href="../../src/verus_syn/item.rs.html#3073-3097"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemType.html" class="struct"
title="struct verus_syn::ImplItemType">ImplItemType</a>

</div>

<div id="impl-Parse-for-Index" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#3315-3330"
class="src rightside">Source</a><a href="#impl-Parse-for-Index" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Index.html" class="struct"
title="struct verus_syn::Index">Index</a>

</div>

<div id="impl-Parse-for-Invariant" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#835-842"
class="src rightside">Source</a><a href="#impl-Parse-for-Invariant" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Invariant.html" class="struct"
title="struct verus_syn::Invariant">Invariant</a>

</div>

<div id="impl-Parse-for-InvariantEnsures" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#845-852"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantEnsures" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::InvariantEnsures">InvariantEnsures</a>

</div>

<div id="impl-Parse-for-InvariantExceptBreak" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#825-832"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantExceptBreak" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::InvariantExceptBreak">InvariantExceptBreak</a>

</div>

<div id="impl-Parse-for-InvariantNameSetAny" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#950-955"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantNameSetAny" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.InvariantNameSetAny.html" class="struct"
title="struct verus_syn::InvariantNameSetAny">InvariantNameSetAny</a>

</div>

<div id="impl-Parse-for-InvariantNameSetList" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#966-976"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantNameSetList" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.InvariantNameSetList.html" class="struct"
title="struct verus_syn::InvariantNameSetList">InvariantNameSetList</a>

</div>

<div id="impl-Parse-for-InvariantNameSetNone" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#958-963"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantNameSetNone" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.InvariantNameSetNone.html" class="struct"
title="struct verus_syn::InvariantNameSetNone">InvariantNameSetNone</a>

</div>

<div id="impl-Parse-for-InvariantNameSetSet" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#979-984"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantNameSetSet" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.InvariantNameSetSet.html" class="struct"
title="struct verus_syn::InvariantNameSetSet">InvariantNameSetSet</a>

</div>

<div id="impl-Parse-for-ItemBroadcastGroup" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1461-1481"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemBroadcastGroup" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemBroadcastGroup.html" class="struct"
title="struct verus_syn::ItemBroadcastGroup">ItemBroadcastGroup</a>

</div>

<div id="impl-Parse-for-ItemConst" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1601-1647"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemConst.html" class="struct"
title="struct verus_syn::ItemConst">ItemConst</a>

</div>

<div id="impl-Parse-for-ItemEnum" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2300-2323"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemEnum" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemEnum.html" class="struct"
title="struct verus_syn::ItemEnum">ItemEnum</a>

</div>

<div id="impl-Parse-for-ItemExternCrate" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1399-1429"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemExternCrate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemExternCrate.html" class="struct"
title="struct verus_syn::ItemExternCrate">ItemExternCrate</a>

</div>

<div id="impl-Parse-for-ItemFn" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1722-1729"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemFn.html" class="struct"
title="struct verus_syn::ItemFn">ItemFn</a>

</div>

<div id="impl-Parse-for-ItemForeignMod" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1997-2019"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemForeignMod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemForeignMod.html" class="struct"
title="struct verus_syn::ItemForeignMod">ItemForeignMod</a>

</div>

<div id="impl-Parse-for-ItemImpl" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2757-2762"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemImpl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemImpl.html" class="struct"
title="struct verus_syn::ItemImpl">ItemImpl</a>

</div>

<div id="impl-Parse-for-ItemMacro" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1345-1373"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemMacro.html" class="struct"
title="struct verus_syn::ItemMacro">ItemMacro</a>

</div>

<div id="impl-Parse-for-ItemMod" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1948-1994"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemMod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemMod.html" class="struct"
title="struct verus_syn::ItemMod">ItemMod</a>

</div>

<div id="impl-Parse-for-ItemStatic" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1550-1598"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemStatic" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemStatic.html" class="struct"
title="struct verus_syn::ItemStatic">ItemStatic</a>

</div>

<div id="impl-Parse-for-ItemStruct" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2274-2297"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemStruct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemStruct.html" class="struct"
title="struct verus_syn::ItemStruct">ItemStruct</a>

</div>

<div id="impl-Parse-for-ItemTrait" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2383-2403"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemTrait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemTrait.html" class="struct"
title="struct verus_syn::ItemTrait">ItemTrait</a>

</div>

<div id="impl-Parse-for-ItemTraitAlias" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2462-2467"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemTraitAlias" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct verus_syn::ItemTraitAlias">ItemTraitAlias</a>

</div>

<div id="impl-Parse-for-ItemType" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2220-2237"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemType.html" class="struct"
title="struct verus_syn::ItemType">ItemType</a>

</div>

<div id="impl-Parse-for-ItemUnion" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2326-2352"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemUnion" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemUnion.html" class="struct"
title="struct verus_syn::ItemUnion">ItemUnion</a>

</div>

<div id="impl-Parse-for-ItemUse" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1432-1437"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemUse" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ItemUse.html" class="struct"
title="struct verus_syn::ItemUse">ItemUse</a>

</div>

<div id="impl-Parse-for-Label" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2966-2973"
class="src rightside">Source</a><a href="#impl-Parse-for-Label" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Label.html" class="struct"
title="struct verus_syn::Label">Label</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Lifetime" class="section impl">

<a href="../../src/verus_syn/lifetime.rs.html#130-138"
class="src rightside">Source</a><a href="#impl-Parse-for-Lifetime" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>

</div>

<div id="impl-Parse-for-LifetimeParam" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#628-663"
class="src rightside">Source</a><a href="#impl-Parse-for-LifetimeParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LifetimeParam.html" class="struct"
title="struct verus_syn::LifetimeParam">LifetimeParam</a>

</div>

<div id="impl-Parse-for-LitBool" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1021-1029"
class="src rightside">Source</a><a href="#impl-Parse-for-LitBool" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitBool.html" class="struct"
title="struct verus_syn::LitBool">LitBool</a>

</div>

<div id="impl-Parse-for-LitByte" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#977-985"
class="src rightside">Source</a><a href="#impl-Parse-for-LitByte" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitByte.html" class="struct"
title="struct verus_syn::LitByte">LitByte</a>

</div>

<div id="impl-Parse-for-LitByteStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#955-963"
class="src rightside">Source</a><a href="#impl-Parse-for-LitByteStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitByteStr.html" class="struct"
title="struct verus_syn::LitByteStr">LitByteStr</a>

</div>

<div id="impl-Parse-for-LitCStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#966-974"
class="src rightside">Source</a><a href="#impl-Parse-for-LitCStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitCStr.html" class="struct"
title="struct verus_syn::LitCStr">LitCStr</a>

</div>

<div id="impl-Parse-for-LitChar" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#988-996"
class="src rightside">Source</a><a href="#impl-Parse-for-LitChar" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitChar.html" class="struct"
title="struct verus_syn::LitChar">LitChar</a>

</div>

<div id="impl-Parse-for-LitFloat" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1010-1018"
class="src rightside">Source</a><a href="#impl-Parse-for-LitFloat" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitFloat.html" class="struct"
title="struct verus_syn::LitFloat">LitFloat</a>

</div>

<div id="impl-Parse-for-LitInt" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#999-1007"
class="src rightside">Source</a><a href="#impl-Parse-for-LitInt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitInt.html" class="struct"
title="struct verus_syn::LitInt">LitInt</a>

</div>

<div id="impl-Parse-for-LitStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#944-952"
class="src rightside">Source</a><a href="#impl-Parse-for-LitStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LitStr.html" class="struct"
title="struct verus_syn::LitStr">LitStr</a>

</div>

<div id="impl-Parse-for-LoopSpec" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#2405-2427"
class="src rightside">Source</a><a href="#impl-Parse-for-LoopSpec" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.LoopSpec.html" class="struct"
title="struct verus_syn::LoopSpec">LoopSpec</a>

</div>

<div id="impl-Parse-for-Macro" class="section impl">

<a href="../../src/verus_syn/mac.rs.html#180-194"
class="src rightside">Source</a><a href="#impl-Parse-for-Macro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Macro.html" class="struct"
title="struct verus_syn::Macro">Macro</a>

</div>

<div id="impl-Parse-for-MetaList" class="section impl">

<a href="../../src/verus_syn/attr.rs.html#695-700"
class="src rightside">Source</a><a href="#impl-Parse-for-MetaList" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.MetaList.html" class="struct"
title="struct verus_syn::MetaList">MetaList</a>

</div>

<div id="impl-Parse-for-MetaNameValue" class="section impl">

<a href="../../src/verus_syn/attr.rs.html#703-708"
class="src rightside">Source</a><a href="#impl-Parse-for-MetaNameValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.MetaNameValue.html" class="struct"
title="struct verus_syn::MetaNameValue">MetaNameValue</a>

</div>

<div id="impl-Parse-for-ParenthesizedGenericArguments"
class="section impl">

<a href="../../src/verus_syn/path.rs.html#496-505"
class="src rightside">Source</a><a href="#impl-Parse-for-ParenthesizedGenericArguments"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct verus_syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>

</div>

<div id="impl-Parse-for-PatType" class="section impl">

<a href="../../src/verus_syn/pat.rs.html#386-395"
class="src rightside">Source</a><a href="#impl-Parse-for-PatType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.PatType.html" class="struct"
title="struct verus_syn::PatType">PatType</a>

</div>

<div id="impl-Parse-for-Path" class="section impl">

<a href="../../src/verus_syn/path.rs.html#309-313"
class="src rightside">Source</a><a href="#impl-Parse-for-Path" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Path.html" class="struct"
title="struct verus_syn::Path">Path</a>

</div>

<div id="impl-Parse-for-PathSegment" class="section impl">

<a href="../../src/verus_syn/path.rs.html#508-512"
class="src rightside">Source</a><a href="#impl-Parse-for-PathSegment" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.PathSegment.html" class="struct"
title="struct verus_syn::PathSegment">PathSegment</a>

</div>

<div id="impl-Parse-for-PreciseCapture" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#1056-1090"
class="src rightside">Source</a><a href="#impl-Parse-for-PreciseCapture" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.PreciseCapture.html" class="struct"
title="struct verus_syn::PreciseCapture">PreciseCapture</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Prover" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#747-759"
class="src rightside">Source</a><a href="#impl-Parse-for-Prover" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Prover.html" class="struct"
title="struct verus_syn::Prover">Prover</a>

</div>

<div id="impl-Parse-for-Receiver" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1834-1876"
class="src rightside">Source</a><a href="#impl-Parse-for-Receiver" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Receiver.html" class="struct"
title="struct verus_syn::Receiver">Receiver</a>

</div>

<div id="impl-Parse-for-Recommends" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#772-786"
class="src rightside">Source</a><a href="#impl-Parse-for-Recommends" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Recommends.html" class="struct"
title="struct verus_syn::Recommends">Recommends</a>

</div>

<div id="impl-Parse-for-Requires" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#762-769"
class="src rightside">Source</a><a href="#impl-Parse-for-Requires" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Requires.html" class="struct"
title="struct verus_syn::Requires">Requires</a>

</div>

<div id="impl-Parse-for-Returns" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#814-822"
class="src rightside">Source</a><a href="#impl-Parse-for-Returns" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::<a href="../struct.Returns.html" class="struct"
title="struct verus_syn::Returns">Returns</a>

</div>

<div id="impl-Parse-for-RevealHide" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1313-1356"
class="src rightside">Source</a><a href="#impl-Parse-for-RevealHide" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.RevealHide.html" class="struct"
title="struct verus_syn::RevealHide">RevealHide</a>

</div>

<div id="impl-Parse-for-Signature" class="section impl">

<a href="../../src/verus_syn/item.rs.html#1665-1670"
class="src rightside">Source</a><a href="#impl-Parse-for-Signature" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Signature.html" class="struct"
title="struct verus_syn::Signature">Signature</a>

</div>

<div id="impl-Parse-for-SignatureDecreases" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#865-888"
class="src rightside">Source</a><a href="#impl-Parse-for-SignatureDecreases" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.SignatureDecreases.html" class="struct"
title="struct verus_syn::SignatureDecreases">SignatureDecreases</a>

</div>

<div id="impl-Parse-for-SignatureInvariants" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#906-916"
class="src rightside">Source</a><a href="#impl-Parse-for-SignatureInvariants" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.SignatureInvariants.html" class="struct"
title="struct verus_syn::SignatureInvariants">SignatureInvariants</a>

</div>

<div id="impl-Parse-for-SignatureSpec" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1119-1145"
class="src rightside">Source</a><a href="#impl-Parse-for-SignatureSpec" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.SignatureSpec.html" class="struct"
title="struct verus_syn::SignatureSpec">SignatureSpec</a>

</div>

<div id="impl-Parse-for-SignatureSpecAttr" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#1148-1172"
class="src rightside">Source</a><a href="#impl-Parse-for-SignatureSpecAttr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.SignatureSpecAttr.html" class="struct"
title="struct verus_syn::SignatureSpecAttr">SignatureSpecAttr</a>

</div>

<div id="impl-Parse-for-SignatureUnwind" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#891-903"
class="src rightside">Source</a><a href="#impl-Parse-for-SignatureUnwind" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.SignatureUnwind.html" class="struct"
title="struct verus_syn::SignatureUnwind">SignatureUnwind</a>

</div>

<div id="impl-Parse-for-Specification" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#693-744"
class="src rightside">Source</a><a href="#impl-Parse-for-Specification" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Specification.html" class="struct"
title="struct verus_syn::Specification">Specification</a>

</div>

<div id="impl-Parse-for-TraitBound" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#824-829"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitBound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TraitBound.html" class="struct"
title="struct verus_syn::TraitBound">TraitBound</a>

</div>

<div id="impl-Parse-for-TraitItemConst" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2612-2650"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemConst.html" class="struct"
title="struct verus_syn::TraitItemConst">TraitItemConst</a>

</div>

<div id="impl-Parse-for-TraitItemFn" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2653-2679"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemFn.html" class="struct"
title="struct verus_syn::TraitItemFn">TraitItemFn</a>

</div>

<div id="impl-Parse-for-TraitItemMacro" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2739-2754"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemMacro.html" class="struct"
title="struct verus_syn::TraitItemMacro">TraitItemMacro</a>

</div>

<div id="impl-Parse-for-TraitItemType" class="section impl">

<a href="../../src/verus_syn/item.rs.html#2682-2703"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemType.html" class="struct"
title="struct verus_syn::TraitItemType">TraitItemType</a>

</div>

<div id="impl-Parse-for-TypeArray" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#653-663"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeArray" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeArray.html" class="struct"
title="struct verus_syn::TypeArray">TypeArray</a>

</div>

<div id="impl-Parse-for-TypeBareFn" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#702-746"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeBareFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeBareFn.html" class="struct"
title="struct verus_syn::TypeBareFn">TypeBareFn</a>

</div>

<div id="impl-Parse-for-TypeGroup" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#1032-1040"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeGroup" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeGroup.html" class="struct"
title="struct verus_syn::TypeGroup">TypeGroup</a>

</div>

<div id="impl-Parse-for-TypeImplTrait" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#966-971"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeImplTrait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeImplTrait.html" class="struct"
title="struct verus_syn::TypeImplTrait">TypeImplTrait</a>

</div>

<div id="impl-Parse-for-TypeInfer" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#758-764"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeInfer" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeInfer.html" class="struct"
title="struct verus_syn::TypeInfer">TypeInfer</a>

</div>

<div id="impl-Parse-for-TypeMacro" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#800-806"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeMacro.html" class="struct"
title="struct verus_syn::TypeMacro">TypeMacro</a>

</div>

<div id="impl-Parse-for-TypeNever" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#749-755"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeNever" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeNever.html" class="struct"
title="struct verus_syn::TypeNever">TypeNever</a>

</div>

<div id="impl-Parse-for-TypeParam" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#699-740"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeParam.html" class="struct"
title="struct verus_syn::TypeParam">TypeParam</a>

</div>

<div id="impl-Parse-for-TypeParen" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#1043-1048"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParen" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeParen.html" class="struct"
title="struct verus_syn::TypeParen">TypeParen</a>

</div>

<div id="impl-Parse-for-TypePath" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#809-815"
class="src rightside">Source</a><a href="#impl-Parse-for-TypePath" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypePath.html" class="struct"
title="struct verus_syn::TypePath">TypePath</a>

</div>

<div id="impl-Parse-for-TypePtr" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#666-686"
class="src rightside">Source</a><a href="#impl-Parse-for-TypePtr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypePtr.html" class="struct"
title="struct verus_syn::TypePtr">TypePtr</a>

</div>

<div id="impl-Parse-for-TypeReference" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#689-699"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeReference" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeReference.html" class="struct"
title="struct verus_syn::TypeReference">TypeReference</a>

</div>

<div id="impl-Parse-for-TypeSlice" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#642-650"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeSlice" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeSlice.html" class="struct"
title="struct verus_syn::TypeSlice">TypeSlice</a>

</div>

<div id="impl-Parse-for-TypeTraitObject" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#902-907"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeTraitObject" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeTraitObject.html" class="struct"
title="struct verus_syn::TypeTraitObject">TypeTraitObject</a>

</div>

<div id="impl-Parse-for-TypeTuple" class="section impl">

<a href="../../src/verus_syn/ty.rs.html#767-797"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeTuple" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.TypeTuple.html" class="struct"
title="struct verus_syn::TypeTuple">TypeTuple</a>

</div>

<div id="impl-Parse-for-Variant" class="section impl">

<a href="../../src/verus_syn/data.rs.html#260-299"
class="src rightside">Source</a><a href="#impl-Parse-for-Variant" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.Variant.html" class="struct"
title="struct verus_syn::Variant">Variant</a>

</div>

<div id="impl-Parse-for-View" class="section impl">

<a href="../../src/verus_syn/expr.rs.html#2641-2655"
class="src rightside">Source</a><a href="#impl-Parse-for-View" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.View.html" class="struct"
title="struct verus_syn::View">View</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-WhereClause" class="section impl">

<a href="../../src/verus_syn/generics.rs.html#927-972"
class="src rightside">Source</a><a href="#impl-Parse-for-WhereClause" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.WhereClause.html" class="struct"
title="struct verus_syn::WhereClause">WhereClause</a>

</div>

<div id="impl-Parse-for-WithSpecOnExpr" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#2502-2541"
class="src rightside">Source</a><a href="#impl-Parse-for-WithSpecOnExpr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.WithSpecOnExpr.html" class="struct"
title="struct verus_syn::WithSpecOnExpr">WithSpecOnExpr</a>

</div>

<div id="impl-Parse-for-WithSpecOnFn" class="section impl">

<a href="../../src/verus_syn/verus.rs.html#2441-2499"
class="src rightside">Source</a><a href="#impl-Parse-for-WithSpecOnFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../struct.WithSpecOnFn.html" class="struct"
title="struct verus_syn::WithSpecOnFn">WithSpecOnFn</a>

</div>

<div id="impl-Parse-for-Abstract" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Abstract" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Abstract.html" class="struct"
title="struct verus_syn::token::Abstract">Abstract</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-And" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-And" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.And.html" class="struct"
title="struct verus_syn::token::And">And</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-AndAnd" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-AndAnd" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.AndAnd.html" class="struct"
title="struct verus_syn::token::AndAnd">AndAnd</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-AndEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-AndEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.AndEq.html" class="struct"
title="struct verus_syn::token::AndEq">AndEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-As" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-As" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.As.html" class="struct"
title="struct verus_syn::token::As">As</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Assert-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Assert-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Assert.html" class="struct"
title="struct verus_syn::token::Assert">Assert</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Assume-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Assume-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Assume.html" class="struct"
title="struct verus_syn::token::Assume">Assume</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-AssumeSpecification-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-AssumeSpecification-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::token::AssumeSpecification">AssumeSpecification</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Async" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Async" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Async.html" class="struct"
title="struct verus_syn::token::Async">Async</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-At" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-At" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.At.html" class="struct"
title="struct verus_syn::token::At">At</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Auto" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Auto" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Auto.html" class="struct"
title="struct verus_syn::token::Auto">Auto</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Await" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Await" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Await.html" class="struct"
title="struct verus_syn::token::Await">Await</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Axiom" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Axiom" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Axiom.html" class="struct"
title="struct verus_syn::token::Axiom">Axiom</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Become" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Become" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Become.html" class="struct"
title="struct verus_syn::token::Become">Become</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-BigAnd" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-BigAnd" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.BigAnd.html" class="struct"
title="struct verus_syn::token::BigAnd">BigAnd</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-BigOr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-BigOr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.BigOr.html" class="struct"
title="struct verus_syn::token::BigOr">BigOr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Box" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Box" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Box.html" class="struct"
title="struct verus_syn::token::Box">Box</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Break" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Break" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Break.html" class="struct"
title="struct verus_syn::token::Break">Break</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Broadcast" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Broadcast" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Broadcast.html" class="struct"
title="struct verus_syn::token::Broadcast">Broadcast</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-BroadcastGroup" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-BroadcastGroup" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.BroadcastGroup.html" class="struct"
title="struct verus_syn::token::BroadcastGroup">BroadcastGroup</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-By" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-By" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.By.html" class="struct"
title="struct verus_syn::token::By">By</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Caret" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Caret" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Caret.html" class="struct"
title="struct verus_syn::token::Caret">Caret</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-CaretEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-CaretEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.CaretEq.html" class="struct"
title="struct verus_syn::token::CaretEq">CaretEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Choose" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Choose" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Choose.html" class="struct"
title="struct verus_syn::token::Choose">Choose</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Closed" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Closed" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Closed.html" class="struct"
title="struct verus_syn::token::Closed">Closed</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Colon" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Colon" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Colon.html" class="struct"
title="struct verus_syn::token::Colon">Colon</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Comma" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Comma" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Comma.html" class="struct"
title="struct verus_syn::token::Comma">Comma</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Const" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Const" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Const.html" class="struct"
title="struct verus_syn::token::Const">Const</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Continue" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Continue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Continue.html" class="struct"
title="struct verus_syn::token::Continue">Continue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Crate" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Crate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Crate.html" class="struct"
title="struct verus_syn::token::Crate">Crate</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Decreases-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Decreases-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Decreases.html" class="struct"
title="struct verus_syn::token::Decreases">Decreases</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Default" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Default" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Default.html" class="struct"
title="struct verus_syn::token::Default">Default</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DefaultEnsures-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-DefaultEnsures-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::token::DefaultEnsures">DefaultEnsures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Do" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Do" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Do.html" class="struct"
title="struct verus_syn::token::Do">Do</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dollar" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Dollar" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Dollar.html" class="struct"
title="struct verus_syn::token::Dollar">Dollar</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Dot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Dot.html" class="struct"
title="struct verus_syn::token::Dot">Dot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDot.html" class="struct"
title="struct verus_syn::token::DotDot">DotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDotDot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDotDot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDotDot.html" class="struct"
title="struct verus_syn::token::DotDotDot">DotDotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDotEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDotEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDotEq.html" class="struct"
title="struct verus_syn::token::DotDotEq">DotDotEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dyn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Dyn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Dyn.html" class="struct"
title="struct verus_syn::token::Dyn">Dyn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Else" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Else" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Else.html" class="struct"
title="struct verus_syn::token::Else">Else</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ensures-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Ensures-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Ensures.html" class="struct"
title="struct verus_syn::token::Ensures">Ensures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Enum" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Enum" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Enum.html" class="struct"
title="struct verus_syn::token::Enum">Enum</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Eq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Eq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Eq.html" class="struct"
title="struct verus_syn::token::Eq">Eq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-EqEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-EqEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.EqEq.html" class="struct"
title="struct verus_syn::token::EqEq">EqEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-EqEqEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-EqEqEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.EqEqEq.html" class="struct"
title="struct verus_syn::token::EqEqEq">EqEqEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Equiv" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Equiv" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Equiv.html" class="struct"
title="struct verus_syn::token::Equiv">Equiv</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Exec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Exec" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Exec.html" class="struct"
title="struct verus_syn::token::Exec">Exec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Exists" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Exists" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Exists.html" class="struct"
title="struct verus_syn::token::Exists">Exists</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Exply" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Exply" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Exply.html" class="struct"
title="struct verus_syn::token::Exply">Exply</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Extern" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Extern" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Extern.html" class="struct"
title="struct verus_syn::token::Extern">Extern</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-FatArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-FatArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.FatArrow.html" class="struct"
title="struct verus_syn::token::FatArrow">FatArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Final" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Final" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Final.html" class="struct"
title="struct verus_syn::token::Final">Final</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Fn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Fn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Fn.html" class="struct"
title="struct verus_syn::token::Fn">Fn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-FnSpec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-FnSpec" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.FnSpec.html" class="struct"
title="struct verus_syn::token::FnSpec">FnSpec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-For" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-For" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.For.html" class="struct"
title="struct verus_syn::token::For">For</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Forall" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Forall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Forall.html" class="struct"
title="struct verus_syn::token::Forall">Forall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ge" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Ge" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Ge.html" class="struct"
title="struct verus_syn::token::Ge">Ge</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ghost" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Ghost" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Ghost.html" class="struct"
title="struct verus_syn::token::Ghost">Ghost</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Global-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Global-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Global.html" class="struct"
title="struct verus_syn::token::Global">Global</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Gt" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Gt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Gt.html" class="struct"
title="struct verus_syn::token::Gt">Gt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Has" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Has" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Has.html" class="struct"
title="struct verus_syn::token::Has">Has</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-HasNot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-HasNot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.HasNot.html" class="struct"
title="struct verus_syn::token::HasNot">HasNot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Hide" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Hide" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Hide.html" class="struct"
title="struct verus_syn::token::Hide">Hide</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-If" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-If" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.If.html" class="struct"
title="struct verus_syn::token::If">If</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Impl" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Impl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Impl.html" class="struct"
title="struct verus_syn::token::Impl">Impl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Implies" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Implies" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Implies.html" class="struct"
title="struct verus_syn::token::Implies">Implies</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Imply" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Imply" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Imply.html" class="struct"
title="struct verus_syn::token::Imply">Imply</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-In" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-In" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.In.html" class="struct"
title="struct verus_syn::token::In">In</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-InvAny" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-InvAny" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.InvAny.html" class="struct"
title="struct verus_syn::token::InvAny">InvAny</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-InvNone" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-InvNone" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.InvNone.html" class="struct"
title="struct verus_syn::token::InvNone">InvNone</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Invariant-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Invariant-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Invariant.html" class="struct"
title="struct verus_syn::token::Invariant">Invariant</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-InvariantEnsures-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantEnsures-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::token::InvariantEnsures">InvariantEnsures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-InvariantExceptBreak-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-InvariantExceptBreak-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::token::InvariantExceptBreak">InvariantExceptBreak</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Is" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Is" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Is.html" class="struct"
title="struct verus_syn::token::Is">Is</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-IsNot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-IsNot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.IsNot.html" class="struct"
title="struct verus_syn::token::IsNot">IsNot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-LArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-LArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.LArrow.html" class="struct"
title="struct verus_syn::token::LArrow">LArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Layout" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Layout" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Layout.html" class="struct"
title="struct verus_syn::token::Layout">Layout</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Le" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Le" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Le.html" class="struct"
title="struct verus_syn::token::Le">Le</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Let" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Let" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Let.html" class="struct"
title="struct verus_syn::token::Let">Let</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Loop" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Loop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Loop.html" class="struct"
title="struct verus_syn::token::Loop">Loop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Lt" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Lt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Lt.html" class="struct"
title="struct verus_syn::token::Lt">Lt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Macro-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Macro-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Macro.html" class="struct"
title="struct verus_syn::token::Macro">Macro</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Match" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Match" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Match.html" class="struct"
title="struct verus_syn::token::Match">Match</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Matches" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Matches" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Matches.html" class="struct"
title="struct verus_syn::token::Matches">Matches</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Minus" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Minus" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Minus.html" class="struct"
title="struct verus_syn::token::Minus">Minus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-MinusEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-MinusEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.MinusEq.html" class="struct"
title="struct verus_syn::token::MinusEq">MinusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Mod" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Mod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Mod.html" class="struct"
title="struct verus_syn::token::Mod">Mod</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Move" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Move" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Move.html" class="struct"
title="struct verus_syn::token::Move">Move</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Mut" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Mut" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Mut.html" class="struct"
title="struct verus_syn::token::Mut">Mut</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ne" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Ne" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Ne.html" class="struct"
title="struct verus_syn::token::Ne">Ne</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-NeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-NeEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.NeEq.html" class="struct"
title="struct verus_syn::token::NeEq">NeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-NoUnwind" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-NoUnwind" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.NoUnwind.html" class="struct"
title="struct verus_syn::token::NoUnwind">NoUnwind</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Not" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Not" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Not.html" class="struct"
title="struct verus_syn::token::Not">Not</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Open" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Open" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Open.html" class="struct"
title="struct verus_syn::token::Open">Open</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-OpensInvariants" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-OpensInvariants" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.OpensInvariants.html" class="struct"
title="struct verus_syn::token::OpensInvariants">OpensInvariants</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Or" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Or" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Or.html" class="struct"
title="struct verus_syn::token::Or">Or</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-OrEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-OrEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.OrEq.html" class="struct"
title="struct verus_syn::token::OrEq">OrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-OrOr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-OrOr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.OrOr.html" class="struct"
title="struct verus_syn::token::OrOr">OrOr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Override" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Override" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Override.html" class="struct"
title="struct verus_syn::token::Override">Override</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PathSep" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-PathSep" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.PathSep.html" class="struct"
title="struct verus_syn::token::PathSep">PathSep</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Percent" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Percent" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Percent.html" class="struct"
title="struct verus_syn::token::Percent">Percent</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PercentEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-PercentEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.PercentEq.html" class="struct"
title="struct verus_syn::token::PercentEq">PercentEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Plus" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Plus" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Plus.html" class="struct"
title="struct verus_syn::token::Plus">Plus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PlusEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-PlusEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.PlusEq.html" class="struct"
title="struct verus_syn::token::PlusEq">PlusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Pound" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Pound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Pound.html" class="struct"
title="struct verus_syn::token::Pound">Pound</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Priv" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Priv" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Priv.html" class="struct"
title="struct verus_syn::token::Priv">Priv</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Proof" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Proof" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Proof.html" class="struct"
title="struct verus_syn::token::Proof">Proof</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-ProofFn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-ProofFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.ProofFn.html" class="struct"
title="struct verus_syn::token::ProofFn">ProofFn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Pub" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Pub" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Pub.html" class="struct"
title="struct verus_syn::token::Pub">Pub</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Question" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Question" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Question.html" class="struct"
title="struct verus_syn::token::Question">Question</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-RArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-RArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.RArrow.html" class="struct"
title="struct verus_syn::token::RArrow">RArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Raw" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Raw" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Raw.html" class="struct"
title="struct verus_syn::token::Raw">Raw</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Recommends-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Recommends-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Recommends.html" class="struct"
title="struct verus_syn::token::Recommends">Recommends</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ref" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Ref" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Ref.html" class="struct"
title="struct verus_syn::token::Ref">Ref</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Requires-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Requires-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Requires.html" class="struct"
title="struct verus_syn::token::Requires">Requires</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Return" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Return" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Return.html" class="struct"
title="struct verus_syn::token::Return">Return</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Returns-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Returns-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Returns.html" class="struct"
title="struct verus_syn::token::Returns">Returns</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Reveal" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Reveal" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Reveal.html" class="struct"
title="struct verus_syn::token::Reveal">Reveal</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-RevealWithFuel" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-RevealWithFuel" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.RevealWithFuel.html" class="struct"
title="struct verus_syn::token::RevealWithFuel">RevealWithFuel</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SelfType" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-SelfType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.SelfType.html" class="struct"
title="struct verus_syn::token::SelfType">SelfType</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SelfValue" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-SelfValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.SelfValue.html" class="struct"
title="struct verus_syn::token::SelfValue">SelfValue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Semi" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Semi" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Semi.html" class="struct"
title="struct verus_syn::token::Semi">Semi</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Shl" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Shl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Shl.html" class="struct"
title="struct verus_syn::token::Shl">Shl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-ShlEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-ShlEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.ShlEq.html" class="struct"
title="struct verus_syn::token::ShlEq">ShlEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Shr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Shr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Shr.html" class="struct"
title="struct verus_syn::token::Shr">Shr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-ShrEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-ShrEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.ShrEq.html" class="struct"
title="struct verus_syn::token::ShrEq">ShrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SizeOf" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-SizeOf" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.SizeOf.html" class="struct"
title="struct verus_syn::token::SizeOf">SizeOf</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Slash" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Slash" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Slash.html" class="struct"
title="struct verus_syn::token::Slash">Slash</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SlashEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-SlashEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.SlashEq.html" class="struct"
title="struct verus_syn::token::SlashEq">SlashEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Spec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Spec" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Spec.html" class="struct"
title="struct verus_syn::token::Spec">Spec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SpecFn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-SpecFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.SpecFn.html" class="struct"
title="struct verus_syn::token::SpecFn">SpecFn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Star" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Star" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Star.html" class="struct"
title="struct verus_syn::token::Star">Star</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-StarEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-StarEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.StarEq.html" class="struct"
title="struct verus_syn::token::StarEq">StarEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Static" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Static" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Static.html" class="struct"
title="struct verus_syn::token::Static">Static</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Struct" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Struct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Struct.html" class="struct"
title="struct verus_syn::token::Struct">Struct</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Super" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Super" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Super.html" class="struct"
title="struct verus_syn::token::Super">Super</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Tilde" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-Tilde" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Tilde.html" class="struct"
title="struct verus_syn::token::Tilde">Tilde</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-TildeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-TildeEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.TildeEq.html" class="struct"
title="struct verus_syn::token::TildeEq">TildeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-TildeNe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-TildeNe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.TildeNe.html" class="struct"
title="struct verus_syn::token::TildeNe">TildeNe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-TildeTildeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-TildeTildeEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.TildeTildeEq.html" class="struct"
title="struct verus_syn::token::TildeTildeEq">TildeTildeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-TildeTildeNe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Parse-for-TildeTildeNe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.TildeTildeNe.html" class="struct"
title="struct verus_syn::token::TildeTildeNe">TildeTildeNe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Tracked" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Tracked" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Tracked.html" class="struct"
title="struct verus_syn::token::Tracked">Tracked</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Trait" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Trait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Trait.html" class="struct"
title="struct verus_syn::token::Trait">Trait</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Try" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Try" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Try.html" class="struct"
title="struct verus_syn::token::Try">Try</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Type-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Type-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for verus_syn::token::<a href="../token/struct.Type.html" class="struct"
title="struct verus_syn::token::Type">Type</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Typeof" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Typeof" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Typeof.html" class="struct"
title="struct verus_syn::token::Typeof">Typeof</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Underscore" class="section impl">

<a href="../../src/verus_syn/token.rs.html#535-551"
class="src rightside">Source</a><a href="#impl-Parse-for-Underscore" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Underscore.html" class="struct"
title="struct verus_syn::token::Underscore">Underscore</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Uninterp" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Uninterp" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Uninterp.html" class="struct"
title="struct verus_syn::token::Uninterp">Uninterp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Union" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Union" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Union.html" class="struct"
title="struct verus_syn::token::Union">Union</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Unsafe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Unsafe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Unsafe.html" class="struct"
title="struct verus_syn::token::Unsafe">Unsafe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Unsized" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Unsized" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Unsized.html" class="struct"
title="struct verus_syn::token::Unsized">Unsized</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Use" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Use" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Use.html" class="struct"
title="struct verus_syn::token::Use">Use</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Via" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Via" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Via.html" class="struct"
title="struct verus_syn::token::Via">Via</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Virtual" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Virtual" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Virtual.html" class="struct"
title="struct verus_syn::token::Virtual">Virtual</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-When" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-When" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.When.html" class="struct"
title="struct verus_syn::token::When">When</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Where" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Where" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Where.html" class="struct"
title="struct verus_syn::token::Where">Where</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-While" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-While" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.While.html" class="struct"
title="struct verus_syn::token::While">While</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-With" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-With" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.With.html" class="struct"
title="struct verus_syn::token::With">With</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Yield" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Parse-for-Yield" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="../token/struct.Yield.html" class="struct"
title="struct verus_syn::token::Yield">Yield</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Nothing" class="section impl">

<a href="../../src/verus_syn/parse.rs.html#1384-1388"
class="src rightside">Source</a><a href="#impl-Parse-for-Nothing" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="struct.Nothing.html" class="struct"
title="struct verus_syn::parse::Nothing">Nothing</a>

</div>

</div>

</div>

</div>
