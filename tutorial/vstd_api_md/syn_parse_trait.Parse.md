<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[parse](index.html)

</div>

# Trait <span class="trait">Parse</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/parse.rs.html#215-217" class="src">Source</a>
</span>

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

Refer to the [module documentation](index.html "mod syn::parse") for
details about implementing and using the `Parse` trait.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.parse" class="section method">

<a href="../../src/syn/parse.rs.html#216"
class="src rightside">Source</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

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

<a href="../../src/syn/parse.rs.html#1192-1199"
class="src rightside">Source</a><a href="#impl-Parse-for-TokenTree" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>

</div>

<div class="impl-items">

<div id="method.parse" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1193-1198"
class="src rightside">Source</a><a href="#method.parse" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CAbi%3E" class="section impl">

<a href="../../src/syn/ty.rs.html#1064-1072"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CAbi%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Abi.html" class="struct"
title="struct syn::Abi">Abi</a>\>

</div>

<div class="impl-items">

<div id="method.parse-1" class="section method trait-impl">

<a href="../../src/syn/ty.rs.html#1065-1071"
class="src rightside">Source</a><a href="#method.parse-1" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CBoundLifetimes%3E"
class="section impl">

<a href="../../src/syn/generics.rs.html#689-697"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CBoundLifetimes%3E"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.BoundLifetimes.html" class="struct"
title="struct syn::BoundLifetimes">BoundLifetimes</a>\>

</div>

<div class="impl-items">

<div id="method.parse-2" class="section method trait-impl">

<a href="../../src/syn/generics.rs.html#690-696"
class="src rightside">Source</a><a href="#method.parse-2" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CLabel%3E" class="section impl">

<a href="../../src/syn/expr.rs.html#2699-2707"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CLabel%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.Label.html" class="struct"
title="struct syn::Label">Label</a>\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.parse-3" class="section method trait-impl">

<a href="../../src/syn/expr.rs.html#2700-2706"
class="src rightside">Source</a><a href="#method.parse-3" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CWhereClause%3E" class="section impl">

<a href="../../src/syn/generics.rs.html#970-978"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CWhereClause%3E" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../struct.WhereClause.html" class="struct"
title="struct syn::WhereClause">WhereClause</a>\>

</div>

<div class="impl-items">

<div id="method.parse-4" class="section method trait-impl">

<a href="../../src/syn/generics.rs.html#971-977"
class="src rightside">Source</a><a href="#method.parse-4" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Group" class="section impl">

<a href="../../src/syn/parse.rs.html#1202-1213"
class="src rightside">Source</a><a href="#impl-Parse-for-Group" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Group.html" class="struct"
title="struct proc_macro2::Group">Group</a>

</div>

<div class="impl-items">

<div id="method.parse-5" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1203-1212"
class="src rightside">Source</a><a href="#method.parse-5" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Literal" class="section impl">

<a href="../../src/syn/parse.rs.html#1226-1233"
class="src rightside">Source</a><a href="#impl-Parse-for-Literal" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.parse-6" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1227-1232"
class="src rightside">Source</a><a href="#method.parse-6" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Punct" class="section impl">

<a href="../../src/syn/parse.rs.html#1216-1223"
class="src rightside">Source</a><a href="#impl-Parse-for-Punct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.Punct.html" class="struct"
title="struct proc_macro2::Punct">Punct</a>

</div>

<div class="impl-items">

<div id="method.parse-7" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1217-1222"
class="src rightside">Source</a><a href="#method.parse-7" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-TokenStream" class="section impl">

<a href="../../src/syn/parse.rs.html#1185-1189"
class="src rightside">Source</a><a href="#impl-Parse-for-TokenStream" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.parse-8" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1186-1188"
class="src rightside">Source</a><a href="#method.parse-8" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Option%3CT%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#1174-1182"
class="src rightside">Source</a><a href="#impl-Parse-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> + <a href="../token/trait.Token.html" class="trait"
title="trait syn::token::Token">Token</a>\> <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.parse-9" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1175-1181"
class="src rightside">Source</a><a href="#method.parse-9" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-Parse-for-Box%3CT%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#1167-1171"
class="src rightside">Source</a><a href="#impl-Parse-for-Box%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a>\> <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/boxed/struct.Box.html"
class="struct" title="struct alloc::boxed::Box">Box</a>\<T\>

</div>

<div class="impl-items">

<div id="method.parse-10" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#1168-1170"
class="src rightside">Source</a><a href="#method.parse-10" class="anchor">§</a>

#### fn <a href="#tymethod.parse" class="fn">parse</a>(input: <a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Parse-for-BinOp" class="section impl">

<a href="../../src/syn/op.rs.html#86-148"
class="src rightside">Source</a><a href="#impl-Parse-for-BinOp" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.BinOp.html" class="enum"
title="enum syn::BinOp">BinOp</a>

</div>

<div id="impl-Parse-for-CapturedParam" class="section impl">

<a href="../../src/syn/generics.rs.html#1089-1100"
class="src rightside">Source</a><a href="#impl-Parse-for-CapturedParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.CapturedParam.html" class="enum"
title="enum syn::CapturedParam">CapturedParam</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Expr" class="section impl">

<a href="../../src/syn/expr.rs.html#1234-1242"
class="src rightside">Source</a><a href="#impl-Parse-for-Expr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>

</div>

<div id="impl-Parse-for-FnArg" class="section impl">

<a href="../../src/syn/item.rs.html#1588-1597"
class="src rightside">Source</a><a href="#impl-Parse-for-FnArg" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.FnArg.html" class="enum"
title="enum syn::FnArg">FnArg</a>

</div>

<div id="impl-Parse-for-ForeignItem" class="section impl">

<a href="../../src/syn/item.rs.html#1843-1939"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.ForeignItem.html" class="enum"
title="enum syn::ForeignItem">ForeignItem</a>

</div>

<div id="impl-Parse-for-GenericArgument" class="section impl">

<a href="../../src/syn/path.rs.html#319-410"
class="src rightside">Source</a><a href="#impl-Parse-for-GenericArgument" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.GenericArgument.html" class="enum"
title="enum syn::GenericArgument">GenericArgument</a>

</div>

<div id="impl-Parse-for-GenericParam" class="section impl">

<a href="../../src/syn/generics.rs.html#602-626"
class="src rightside">Source</a><a href="#impl-Parse-for-GenericParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.GenericParam.html" class="enum"
title="enum syn::GenericParam">GenericParam</a>

</div>

<div id="impl-Parse-for-ImplItem" class="section impl">

<a href="../../src/syn/item.rs.html#2664-2757"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.ImplItem.html" class="enum"
title="enum syn::ImplItem">ImplItem</a>

</div>

<div id="impl-Parse-for-Item" class="section impl">

<a href="../../src/syn/item.rs.html#942-948"
class="src rightside">Source</a><a href="#impl-Parse-for-Item" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Item.html" class="enum" title="enum syn::Item">Item</a>

</div>

<div id="impl-Parse-for-Lit" class="section impl">

<a href="../../src/syn/lit.rs.html#881-910"
class="src rightside">Source</a><a href="#impl-Parse-for-Lit" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Lit.html" class="enum" title="enum syn::Lit">Lit</a>

</div>

<div id="impl-Parse-for-Member" class="section impl">

<a href="../../src/syn/expr.rs.html#2979-2989"
class="src rightside">Source</a><a href="#impl-Parse-for-Member" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Member.html" class="enum"
title="enum syn::Member">Member</a>

</div>

<div id="impl-Parse-for-Meta" class="section impl">

<a href="../../src/syn/attr.rs.html#692-697"
class="src rightside">Source</a><a href="#impl-Parse-for-Meta" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Meta.html" class="enum" title="enum syn::Meta">Meta</a>

</div>

<div id="impl-Parse-for-PointerMutability" class="section impl">

<a href="../../src/syn/expr.rs.html#3090-3101"
class="src rightside">Source</a><a href="#impl-Parse-for-PointerMutability" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.PointerMutability.html" class="enum"
title="enum syn::PointerMutability">PointerMutability</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-RangeLimits" class="section impl">

<a href="../../src/syn/expr.rs.html#2927-2941"
class="src rightside">Source</a><a href="#impl-Parse-for-RangeLimits" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.RangeLimits.html" class="enum"
title="enum syn::RangeLimits">RangeLimits</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ReturnType" class="section impl">

<a href="../../src/syn/ty.rs.html#813-818"
class="src rightside">Source</a><a href="#impl-Parse-for-ReturnType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.ReturnType.html" class="enum"
title="enum syn::ReturnType">ReturnType</a>

</div>

<div id="impl-Parse-for-StaticMutability" class="section impl">

<a href="../../src/syn/item.rs.html#2927-2932"
class="src rightside">Source</a><a href="#impl-Parse-for-StaticMutability" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.StaticMutability.html" class="enum"
title="enum syn::StaticMutability">StaticMutability</a>

</div>

<div id="impl-Parse-for-Stmt" class="section impl">

<a href="../../src/syn/stmt.rs.html#195-200"
class="src rightside">Source</a><a href="#impl-Parse-for-Stmt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Stmt.html" class="enum" title="enum syn::Stmt">Stmt</a>

</div>

<div id="impl-Parse-for-TraitBoundModifier" class="section impl">

<a href="../../src/syn/generics.rs.html#897-905"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitBoundModifier" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum syn::TraitBoundModifier">TraitBoundModifier</a>

</div>

<div id="impl-Parse-for-TraitItem" class="section impl">

<a href="../../src/syn/item.rs.html#2333-2416"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItem" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.TraitItem.html" class="enum"
title="enum syn::TraitItem">TraitItem</a>

</div>

<div id="impl-Parse-for-Type" class="section impl">

<a href="../../src/syn/ty.rs.html#300-306"
class="src rightside">Source</a><a href="#impl-Parse-for-Type" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for syn::<a href="../enum.Type.html" class="enum" title="enum syn::Type">Type</a>

</div>

<div id="impl-Parse-for-TypeParamBound" class="section impl">

<a href="../../src/syn/generics.rs.html#748-754"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParamBound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.TypeParamBound.html" class="enum"
title="enum syn::TypeParamBound">TypeParamBound</a>

</div>

<div id="impl-Parse-for-UnOp" class="section impl">

<a href="../../src/syn/op.rs.html#151-164"
class="src rightside">Source</a><a href="#impl-Parse-for-UnOp" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.UnOp.html" class="enum" title="enum syn::UnOp">UnOp</a>

</div>

<div id="impl-Parse-for-UseTree" class="section impl">

<a href="../../src/syn/item.rs.html#1361-1366"
class="src rightside">Source</a><a href="#impl-Parse-for-UseTree" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.UseTree.html" class="enum"
title="enum syn::UseTree">UseTree</a>

</div>

<div id="impl-Parse-for-Visibility" class="section impl">

<a href="../../src/syn/restriction.rs.html#73-92"
class="src rightside">Source</a><a href="#impl-Parse-for-Visibility" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.Visibility.html" class="enum"
title="enum syn::Visibility">Visibility</a>

</div>

<div id="impl-Parse-for-WherePredicate" class="section impl">

<a href="../../src/syn/generics.rs.html#981-1047"
class="src rightside">Source</a><a href="#impl-Parse-for-WherePredicate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../enum.WherePredicate.html" class="enum"
title="enum syn::WherePredicate">WherePredicate</a>

</div>

<div id="impl-Parse-for-Abi" class="section impl">

<a href="../../src/syn/ty.rs.html#1054-1061"
class="src rightside">Source</a><a href="#impl-Parse-for-Abi" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Abi.html" class="struct"
title="struct syn::Abi">Abi</a>

</div>

<div id="impl-Parse-for-AngleBracketedGenericArguments"
class="section impl">

<a href="../../src/syn/path.rs.html#491-496"
class="src rightside">Source</a><a href="#impl-Parse-for-AngleBracketedGenericArguments"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>

</div>

<div id="impl-Parse-for-Arm" class="section impl">

<a href="../../src/syn/expr.rs.html#3004-3034"
class="src rightside">Source</a><a href="#impl-Parse-for-Arm" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Arm.html" class="struct"
title="struct syn::Arm">Arm</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-BareFnArg" class="section impl">

<a href="../../src/syn/ty.rs.html#983-988"
class="src rightside">Source</a><a href="#impl-Parse-for-BareFnArg" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.BareFnArg.html" class="struct"
title="struct syn::BareFnArg">BareFnArg</a>

</div>

<div id="impl-Parse-for-Block" class="section impl">

<a href="../../src/syn/stmt.rs.html#184-192"
class="src rightside">Source</a><a href="#impl-Parse-for-Block" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Block.html" class="struct"
title="struct syn::Block">Block</a>

</div>

<div id="impl-Parse-for-BoundLifetimes" class="section impl">

<a href="../../src/syn/generics.rs.html#667-686"
class="src rightside">Source</a><a href="#impl-Parse-for-BoundLifetimes" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.BoundLifetimes.html" class="struct"
title="struct syn::BoundLifetimes">BoundLifetimes</a>

</div>

<div id="impl-Parse-for-ConstParam" class="section impl">

<a href="../../src/syn/generics.rs.html#908-929"
class="src rightside">Source</a><a href="#impl-Parse-for-ConstParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ConstParam.html" class="struct"
title="struct syn::ConstParam">ConstParam</a>

</div>

<div id="impl-Parse-for-DeriveInput" class="section impl">

<a href="../../src/syn/derive.rs.html#81-147"
class="src rightside">Source</a><a href="#impl-Parse-for-DeriveInput" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.DeriveInput.html" class="struct"
title="struct syn::DeriveInput">DeriveInput</a>

</div>

<div id="impl-Parse-for-ExprArray" class="section impl">

<a href="../../src/syn/expr.rs.html#2094-2116"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprArray" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAssign" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAssign" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAsync" class="section impl">

<a href="../../src/syn/expr.rs.html#2596-2605"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAsync" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprAwait" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprAwait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBinary" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBinary" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBlock" class="section impl">

<a href="../../src/syn/expr.rs.html#2859-2875"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBlock" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprBreak" class="section impl">

<a href="../../src/syn/expr.rs.html#2475-2480"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprBreak" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprCall" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprCall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprCast" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprCast" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprClosure" class="section impl">

<a href="../../src/syn/expr.rs.html#2437-2442"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprClosure" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprConst" class="section impl">

<a href="../../src/syn/expr.rs.html#2669-2684"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprContinue" class="section impl">

<a href="../../src/syn/expr.rs.html#2711-2719"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprContinue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprField" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprField" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprForLoop" class="section impl">

<a href="../../src/syn/expr.rs.html#2299-2325"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprForLoop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprIf" class="section impl">

<a href="../../src/syn/expr.rs.html#2234-2284"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprIf" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprIndex" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprIndex" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprInfer" class="section impl">

<a href="../../src/syn/expr.rs.html#2288-2295"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprInfer" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprLet" class="section impl">

<a href="../../src/syn/expr.rs.html#2211-2216"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLet" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprLit" class="section impl">

<a href="../../src/syn/expr.rs.html#2153-2160"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLit" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>

</div>

<div id="impl-Parse-for-ExprLoop" class="section impl">

<a href="../../src/syn/expr.rs.html#2329-2347"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprLoop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprMacro" class="section impl">

<a href="../../src/syn/expr.rs.html#2000-2007"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>

</div>

<div id="impl-Parse-for-ExprMatch" class="section impl">

<a href="../../src/syn/expr.rs.html#2351-2371"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMatch" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprMethodCall" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprMethodCall" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprParen" class="section impl">

<a href="../../src/syn/expr.rs.html#2198-2207"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprParen" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprPath" class="section impl">

<a href="../../src/syn/expr.rs.html#2964-2976"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprPath" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>

</div>

<div id="impl-Parse-for-ExprRange" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRange" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprRawAddr" class="section impl">

<a href="../../src/syn/expr.rs.html#2446-2457"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRawAddr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprReference" class="section impl">

<a href="../../src/syn/expr.rs.html#2461-2471"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprReference" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprRepeat" class="section impl">

<a href="../../src/syn/expr.rs.html#2120-2131"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprRepeat" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprReturn" class="section impl">

<a href="../../src/syn/expr.rs.html#2484-2498"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprReturn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprStruct" class="section impl">

<a href="../../src/syn/expr.rs.html#2785-2791"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprStruct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>

</div>

<div id="impl-Parse-for-ExprTry" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTry" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprTryBlock" class="section impl">

<a href="../../src/syn/expr.rs.html#2510-2518"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTryBlock" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprTuple" class="section impl">

<a href="../../src/syn/expr.rs.html#2398-2410"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprTuple" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `full` and `printing`** only.

</div>

</div>

<div id="impl-Parse-for-ExprUnary" class="section impl">

<a href="../../src/syn/expr.rs.html#2414-2420"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprUnary" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprUnsafe" class="section impl">

<a href="../../src/syn/expr.rs.html#2840-2855"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprUnsafe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprWhile" class="section impl">

<a href="../../src/syn/expr.rs.html#2645-2665"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprWhile" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-ExprYield" class="section impl">

<a href="../../src/syn/expr.rs.html#2522-2536"
class="src rightside">Source</a><a href="#impl-Parse-for-ExprYield" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-FieldValue" class="section impl">

<a href="../../src/syn/expr.rs.html#2756-2782"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.FieldValue.html" class="struct"
title="struct syn::FieldValue">FieldValue</a>

</div>

<div id="impl-Parse-for-FieldsNamed" class="section impl">

<a href="../../src/syn/data.rs.html#301-309"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldsNamed" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.FieldsNamed.html" class="struct"
title="struct syn::FieldsNamed">FieldsNamed</a>

</div>

<div id="impl-Parse-for-FieldsUnnamed" class="section impl">

<a href="../../src/syn/data.rs.html#312-320"
class="src rightside">Source</a><a href="#impl-Parse-for-FieldsUnnamed" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct syn::FieldsUnnamed">FieldsUnnamed</a>

</div>

<div id="impl-Parse-for-File" class="section impl">

<a href="../../src/syn/file.rs.html#97-111"
class="src rightside">Source</a><a href="#impl-Parse-for-File" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.File.html" class="struct"
title="struct syn::File">File</a>

</div>

<div id="impl-Parse-for-ForeignItemFn" class="section impl">

<a href="../../src/syn/item.rs.html#1942-1955"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemFn.html" class="struct"
title="struct syn::ForeignItemFn">ForeignItemFn</a>

</div>

<div id="impl-Parse-for-ForeignItemMacro" class="section impl">

<a href="../../src/syn/item.rs.html#2023-2038"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct syn::ForeignItemMacro">ForeignItemMacro</a>

</div>

<div id="impl-Parse-for-ForeignItemStatic" class="section impl">

<a href="../../src/syn/item.rs.html#1958-1971"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemStatic" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct syn::ForeignItemStatic">ForeignItemStatic</a>

</div>

<div id="impl-Parse-for-ForeignItemType" class="section impl">

<a href="../../src/syn/item.rs.html#1974-1989"
class="src rightside">Source</a><a href="#impl-Parse-for-ForeignItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ForeignItemType.html" class="struct"
title="struct syn::ForeignItemType">ForeignItemType</a>

</div>

<div id="impl-Parse-for-Generics" class="section impl">

<a href="../../src/syn/generics.rs.html#539-599"
class="src rightside">Source</a><a href="#impl-Parse-for-Generics" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Generics.html" class="struct"
title="struct syn::Generics">Generics</a>

</div>

<div id="impl-Parse-for-Ident" class="section impl">

<a href="../../src/syn/ident.rs.html#77-94"
class="src rightside">Source</a><a href="#impl-Parse-for-Ident" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Ident.html" class="struct"
title="struct syn::Ident">Ident</a>

</div>

<div id="impl-Parse-for-ImplItemConst" class="section impl">

<a href="../../src/syn/item.rs.html#2760-2794"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemConst.html" class="struct"
title="struct syn::ImplItemConst">ImplItemConst</a>

</div>

<div id="impl-Parse-for-ImplItemFn" class="section impl">

<a href="../../src/syn/item.rs.html#2797-2802"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemFn.html" class="struct"
title="struct syn::ImplItemFn">ImplItemFn</a>

</div>

<div id="impl-Parse-for-ImplItemMacro" class="section impl">

<a href="../../src/syn/item.rs.html#2900-2915"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemMacro.html" class="struct"
title="struct syn::ImplItemMacro">ImplItemMacro</a>

</div>

<div id="impl-Parse-for-ImplItemType" class="section impl">

<a href="../../src/syn/item.rs.html#2838-2862"
class="src rightside">Source</a><a href="#impl-Parse-for-ImplItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ImplItemType.html" class="struct"
title="struct syn::ImplItemType">ImplItemType</a>

</div>

<div id="impl-Parse-for-Index" class="section impl">

<a href="../../src/syn/expr.rs.html#3037-3052"
class="src rightside">Source</a><a href="#impl-Parse-for-Index" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Index.html" class="struct"
title="struct syn::Index">Index</a>

</div>

<div id="impl-Parse-for-ItemConst" class="section impl">

<a href="../../src/syn/item.rs.html#1463-1495"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemConst.html" class="struct"
title="struct syn::ItemConst">ItemConst</a>

</div>

<div id="impl-Parse-for-ItemEnum" class="section impl">

<a href="../../src/syn/item.rs.html#2119-2140"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemEnum" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemEnum.html" class="struct"
title="struct syn::ItemEnum">ItemEnum</a>

</div>

<div id="impl-Parse-for-ItemExternCrate" class="section impl">

<a href="../../src/syn/item.rs.html#1294-1324"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemExternCrate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemExternCrate.html" class="struct"
title="struct syn::ItemExternCrate">ItemExternCrate</a>

</div>

<div id="impl-Parse-for-ItemFn" class="section impl">

<a href="../../src/syn/item.rs.html#1559-1566"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemFn.html" class="struct"
title="struct syn::ItemFn">ItemFn</a>

</div>

<div id="impl-Parse-for-ItemForeignMod" class="section impl">

<a href="../../src/syn/item.rs.html#1818-1840"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemForeignMod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemForeignMod.html" class="struct"
title="struct syn::ItemForeignMod">ItemForeignMod</a>

</div>

<div id="impl-Parse-for-ItemImpl" class="section impl">

<a href="../../src/syn/item.rs.html#2560-2565"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemImpl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemImpl.html" class="struct"
title="struct syn::ItemImpl">ItemImpl</a>

</div>

<div id="impl-Parse-for-ItemMacro" class="section impl">

<a href="../../src/syn/item.rs.html#1240-1268"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemMacro.html" class="struct"
title="struct syn::ItemMacro">ItemMacro</a>

</div>

<div id="impl-Parse-for-ItemMod" class="section impl">

<a href="../../src/syn/item.rs.html#1769-1815"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemMod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemMod.html" class="struct"
title="struct syn::ItemMod">ItemMod</a>

</div>

<div id="impl-Parse-for-ItemStatic" class="section impl">

<a href="../../src/syn/item.rs.html#1445-1460"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemStatic" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemStatic.html" class="struct"
title="struct syn::ItemStatic">ItemStatic</a>

</div>

<div id="impl-Parse-for-ItemStruct" class="section impl">

<a href="../../src/syn/item.rs.html#2095-2116"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemStruct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemStruct.html" class="struct"
title="struct syn::ItemStruct">ItemStruct</a>

</div>

<div id="impl-Parse-for-ItemTrait" class="section impl">

<a href="../../src/syn/item.rs.html#2194-2214"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemTrait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemTrait.html" class="struct"
title="struct syn::ItemTrait">ItemTrait</a>

</div>

<div id="impl-Parse-for-ItemTraitAlias" class="section impl">

<a href="../../src/syn/item.rs.html#2273-2278"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemTraitAlias" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct syn::ItemTraitAlias">ItemTraitAlias</a>

</div>

<div id="impl-Parse-for-ItemType" class="section impl">

<a href="../../src/syn/item.rs.html#2041-2058"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemType.html" class="struct"
title="struct syn::ItemType">ItemType</a>

</div>

<div id="impl-Parse-for-ItemUnion" class="section impl">

<a href="../../src/syn/item.rs.html#2143-2163"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemUnion" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemUnion.html" class="struct"
title="struct syn::ItemUnion">ItemUnion</a>

</div>

<div id="impl-Parse-for-ItemUse" class="section impl">

<a href="../../src/syn/item.rs.html#1327-1332"
class="src rightside">Source</a><a href="#impl-Parse-for-ItemUse" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ItemUse.html" class="struct"
title="struct syn::ItemUse">ItemUse</a>

</div>

<div id="impl-Parse-for-Label" class="section impl">

<a href="../../src/syn/expr.rs.html#2688-2695"
class="src rightside">Source</a><a href="#impl-Parse-for-Label" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Label.html" class="struct"
title="struct syn::Label">Label</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Lifetime" class="section impl">

<a href="../../src/syn/lifetime.rs.html#130-138"
class="src rightside">Source</a><a href="#impl-Parse-for-Lifetime" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Lifetime.html" class="struct"
title="struct syn::Lifetime">Lifetime</a>

</div>

<div id="impl-Parse-for-LifetimeParam" class="section impl">

<a href="../../src/syn/generics.rs.html#629-664"
class="src rightside">Source</a><a href="#impl-Parse-for-LifetimeParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LifetimeParam.html" class="struct"
title="struct syn::LifetimeParam">LifetimeParam</a>

</div>

<div id="impl-Parse-for-LitBool" class="section impl">

<a href="../../src/syn/lit.rs.html#1029-1037"
class="src rightside">Source</a><a href="#impl-Parse-for-LitBool" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitBool.html" class="struct"
title="struct syn::LitBool">LitBool</a>

</div>

<div id="impl-Parse-for-LitByte" class="section impl">

<a href="../../src/syn/lit.rs.html#985-993"
class="src rightside">Source</a><a href="#impl-Parse-for-LitByte" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitByte.html" class="struct"
title="struct syn::LitByte">LitByte</a>

</div>

<div id="impl-Parse-for-LitByteStr" class="section impl">

<a href="../../src/syn/lit.rs.html#963-971"
class="src rightside">Source</a><a href="#impl-Parse-for-LitByteStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitByteStr.html" class="struct"
title="struct syn::LitByteStr">LitByteStr</a>

</div>

<div id="impl-Parse-for-LitCStr" class="section impl">

<a href="../../src/syn/lit.rs.html#974-982"
class="src rightside">Source</a><a href="#impl-Parse-for-LitCStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitCStr.html" class="struct"
title="struct syn::LitCStr">LitCStr</a>

</div>

<div id="impl-Parse-for-LitChar" class="section impl">

<a href="../../src/syn/lit.rs.html#996-1004"
class="src rightside">Source</a><a href="#impl-Parse-for-LitChar" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitChar.html" class="struct"
title="struct syn::LitChar">LitChar</a>

</div>

<div id="impl-Parse-for-LitFloat" class="section impl">

<a href="../../src/syn/lit.rs.html#1018-1026"
class="src rightside">Source</a><a href="#impl-Parse-for-LitFloat" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitFloat.html" class="struct"
title="struct syn::LitFloat">LitFloat</a>

</div>

<div id="impl-Parse-for-LitInt" class="section impl">

<a href="../../src/syn/lit.rs.html#1007-1015"
class="src rightside">Source</a><a href="#impl-Parse-for-LitInt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitInt.html" class="struct"
title="struct syn::LitInt">LitInt</a>

</div>

<div id="impl-Parse-for-LitStr" class="section impl">

<a href="../../src/syn/lit.rs.html#952-960"
class="src rightside">Source</a><a href="#impl-Parse-for-LitStr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.LitStr.html" class="struct"
title="struct syn::LitStr">LitStr</a>

</div>

<div id="impl-Parse-for-Macro" class="section impl">

<a href="../../src/syn/mac.rs.html#180-194"
class="src rightside">Source</a><a href="#impl-Parse-for-Macro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for syn::<a href="../struct.Macro.html" class="struct"
title="struct syn::Macro">Macro</a>

</div>

<div id="impl-Parse-for-MetaList" class="section impl">

<a href="../../src/syn/attr.rs.html#700-705"
class="src rightside">Source</a><a href="#impl-Parse-for-MetaList" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.MetaList.html" class="struct"
title="struct syn::MetaList">MetaList</a>

</div>

<div id="impl-Parse-for-MetaNameValue" class="section impl">

<a href="../../src/syn/attr.rs.html#708-713"
class="src rightside">Source</a><a href="#impl-Parse-for-MetaNameValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.MetaNameValue.html" class="struct"
title="struct syn::MetaNameValue">MetaNameValue</a>

</div>

<div id="impl-Parse-for-ParenthesizedGenericArguments"
class="section impl">

<a href="../../src/syn/path.rs.html#499-508"
class="src rightside">Source</a><a href="#impl-Parse-for-ParenthesizedGenericArguments"
class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>

</div>

<div id="impl-Parse-for-PatType" class="section impl">

<a href="../../src/syn/pat.rs.html#390-399"
class="src rightside">Source</a><a href="#impl-Parse-for-PatType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>

</div>

<div id="impl-Parse-for-Path" class="section impl">

<a href="../../src/syn/path.rs.html#312-316"
class="src rightside">Source</a><a href="#impl-Parse-for-Path" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Path.html" class="struct"
title="struct syn::Path">Path</a>

</div>

<div id="impl-Parse-for-PathSegment" class="section impl">

<a href="../../src/syn/path.rs.html#511-515"
class="src rightside">Source</a><a href="#impl-Parse-for-PathSegment" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.PathSegment.html" class="struct"
title="struct syn::PathSegment">PathSegment</a>

</div>

<div id="impl-Parse-for-PreciseCapture" class="section impl">

<a href="../../src/syn/generics.rs.html#1051-1085"
class="src rightside">Source</a><a href="#impl-Parse-for-PreciseCapture" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.PreciseCapture.html" class="struct"
title="struct syn::PreciseCapture">PreciseCapture</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `full`** only.

</div>

</div>

<div id="impl-Parse-for-Receiver" class="section impl">

<a href="../../src/syn/item.rs.html#1655-1697"
class="src rightside">Source</a><a href="#impl-Parse-for-Receiver" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Receiver.html" class="struct"
title="struct syn::Receiver">Receiver</a>

</div>

<div id="impl-Parse-for-Signature" class="section impl">

<a href="../../src/syn/item.rs.html#1510-1515"
class="src rightside">Source</a><a href="#impl-Parse-for-Signature" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Signature.html" class="struct"
title="struct syn::Signature">Signature</a>

</div>

<div id="impl-Parse-for-TraitBound" class="section impl">

<a href="../../src/syn/generics.rs.html#829-834"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitBound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TraitBound.html" class="struct"
title="struct syn::TraitBound">TraitBound</a>

</div>

<div id="impl-Parse-for-TraitItemConst" class="section impl">

<a href="../../src/syn/item.rs.html#2419-2453"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemConst" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemConst.html" class="struct"
title="struct syn::TraitItemConst">TraitItemConst</a>

</div>

<div id="impl-Parse-for-TraitItemFn" class="section impl">

<a href="../../src/syn/item.rs.html#2456-2482"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemFn.html" class="struct"
title="struct syn::TraitItemFn">TraitItemFn</a>

</div>

<div id="impl-Parse-for-TraitItemMacro" class="section impl">

<a href="../../src/syn/item.rs.html#2542-2557"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemMacro.html" class="struct"
title="struct syn::TraitItemMacro">TraitItemMacro</a>

</div>

<div id="impl-Parse-for-TraitItemType" class="section impl">

<a href="../../src/syn/item.rs.html#2485-2506"
class="src rightside">Source</a><a href="#impl-Parse-for-TraitItemType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TraitItemType.html" class="struct"
title="struct syn::TraitItemType">TraitItemType</a>

</div>

<div id="impl-Parse-for-TypeArray" class="section impl">

<a href="../../src/syn/ty.rs.html#629-639"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeArray" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeArray.html" class="struct"
title="struct syn::TypeArray">TypeArray</a>

</div>

<div id="impl-Parse-for-TypeBareFn" class="section impl">

<a href="../../src/syn/ty.rs.html#678-722"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeBareFn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeBareFn.html" class="struct"
title="struct syn::TypeBareFn">TypeBareFn</a>

</div>

<div id="impl-Parse-for-TypeGroup" class="section impl">

<a href="../../src/syn/ty.rs.html#951-959"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeGroup" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeGroup.html" class="struct"
title="struct syn::TypeGroup">TypeGroup</a>

</div>

<div id="impl-Parse-for-TypeImplTrait" class="section impl">

<a href="../../src/syn/ty.rs.html#885-890"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeImplTrait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeImplTrait.html" class="struct"
title="struct syn::TypeImplTrait">TypeImplTrait</a>

</div>

<div id="impl-Parse-for-TypeInfer" class="section impl">

<a href="../../src/syn/ty.rs.html#734-740"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeInfer" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeInfer.html" class="struct"
title="struct syn::TypeInfer">TypeInfer</a>

</div>

<div id="impl-Parse-for-TypeMacro" class="section impl">

<a href="../../src/syn/ty.rs.html#776-782"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeMacro" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeMacro.html" class="struct"
title="struct syn::TypeMacro">TypeMacro</a>

</div>

<div id="impl-Parse-for-TypeNever" class="section impl">

<a href="../../src/syn/ty.rs.html#725-731"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeNever" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeNever.html" class="struct"
title="struct syn::TypeNever">TypeNever</a>

</div>

<div id="impl-Parse-for-TypeParam" class="section impl">

<a href="../../src/syn/generics.rs.html#700-745"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParam" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeParam.html" class="struct"
title="struct syn::TypeParam">TypeParam</a>

</div>

<div id="impl-Parse-for-TypeParen" class="section impl">

<a href="../../src/syn/ty.rs.html#962-967"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeParen" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeParen.html" class="struct"
title="struct syn::TypeParen">TypeParen</a>

</div>

<div id="impl-Parse-for-TypePath" class="section impl">

<a href="../../src/syn/ty.rs.html#785-791"
class="src rightside">Source</a><a href="#impl-Parse-for-TypePath" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypePath.html" class="struct"
title="struct syn::TypePath">TypePath</a>

</div>

<div id="impl-Parse-for-TypePtr" class="section impl">

<a href="../../src/syn/ty.rs.html#642-662"
class="src rightside">Source</a><a href="#impl-Parse-for-TypePtr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypePtr.html" class="struct"
title="struct syn::TypePtr">TypePtr</a>

</div>

<div id="impl-Parse-for-TypeReference" class="section impl">

<a href="../../src/syn/ty.rs.html#665-675"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeReference" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeReference.html" class="struct"
title="struct syn::TypeReference">TypeReference</a>

</div>

<div id="impl-Parse-for-TypeSlice" class="section impl">

<a href="../../src/syn/ty.rs.html#618-626"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeSlice" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeSlice.html" class="struct"
title="struct syn::TypeSlice">TypeSlice</a>

</div>

<div id="impl-Parse-for-TypeTraitObject" class="section impl">

<a href="../../src/syn/ty.rs.html#821-826"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeTraitObject" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeTraitObject.html" class="struct"
title="struct syn::TypeTraitObject">TypeTraitObject</a>

</div>

<div id="impl-Parse-for-TypeTuple" class="section impl">

<a href="../../src/syn/ty.rs.html#743-773"
class="src rightside">Source</a><a href="#impl-Parse-for-TypeTuple" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.TypeTuple.html" class="struct"
title="struct syn::TypeTuple">TypeTuple</a>

</div>

<div id="impl-Parse-for-Variant" class="section impl">

<a href="../../src/syn/data.rs.html#259-298"
class="src rightside">Source</a><a href="#impl-Parse-for-Variant" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.Variant.html" class="struct"
title="struct syn::Variant">Variant</a>

</div>

<div id="impl-Parse-for-WhereClause" class="section impl">

<a href="../../src/syn/generics.rs.html#932-967"
class="src rightside">Source</a><a href="#impl-Parse-for-WhereClause" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../struct.WhereClause.html" class="struct"
title="struct syn::WhereClause">WhereClause</a>

</div>

<div id="impl-Parse-for-Abstract" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Abstract" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Abstract.html" class="struct"
title="struct syn::token::Abstract">Abstract</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-And" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-And" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.And.html" class="struct"
title="struct syn::token::And">And</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-AndAnd" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-AndAnd" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.AndAnd.html" class="struct"
title="struct syn::token::AndAnd">AndAnd</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-AndEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-AndEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.AndEq.html" class="struct"
title="struct syn::token::AndEq">AndEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-As" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-As" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.As.html" class="struct"
title="struct syn::token::As">As</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Async" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Async" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Async.html" class="struct"
title="struct syn::token::Async">Async</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-At" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-At" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.At.html" class="struct"
title="struct syn::token::At">At</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Auto" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Auto" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Auto.html" class="struct"
title="struct syn::token::Auto">Auto</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Await" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Await" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Await.html" class="struct"
title="struct syn::token::Await">Await</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Become" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Become" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Become.html" class="struct"
title="struct syn::token::Become">Become</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Box" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Box" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for syn::token::<a href="../token/struct.Box.html" class="struct"
title="struct syn::token::Box">Box</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Break" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Break" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Break.html" class="struct"
title="struct syn::token::Break">Break</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Caret" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Caret" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Caret.html" class="struct"
title="struct syn::token::Caret">Caret</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-CaretEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-CaretEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.CaretEq.html" class="struct"
title="struct syn::token::CaretEq">CaretEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Colon" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Colon" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Colon.html" class="struct"
title="struct syn::token::Colon">Colon</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Comma" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Comma" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Comma.html" class="struct"
title="struct syn::token::Comma">Comma</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Const" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Const" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Const.html" class="struct"
title="struct syn::token::Const">Const</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Continue" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Continue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Continue.html" class="struct"
title="struct syn::token::Continue">Continue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Crate" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Crate" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Crate.html" class="struct"
title="struct syn::token::Crate">Crate</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Default" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Default" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Default.html" class="struct"
title="struct syn::token::Default">Default</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Do" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Do" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Do.html" class="struct"
title="struct syn::token::Do">Do</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dollar" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Dollar" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Dollar.html" class="struct"
title="struct syn::token::Dollar">Dollar</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dot" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Dot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Dot.html" class="struct"
title="struct syn::token::Dot">Dot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDot" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDot.html" class="struct"
title="struct syn::token::DotDot">DotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDotDot" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDotDot" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDotDot.html" class="struct"
title="struct syn::token::DotDotDot">DotDotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-DotDotEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-DotDotEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.DotDotEq.html" class="struct"
title="struct syn::token::DotDotEq">DotDotEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Dyn" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Dyn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Dyn.html" class="struct"
title="struct syn::token::Dyn">Dyn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Else" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Else" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Else.html" class="struct"
title="struct syn::token::Else">Else</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Enum" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Enum" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Enum.html" class="struct"
title="struct syn::token::Enum">Enum</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Eq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Eq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Eq.html" class="struct"
title="struct syn::token::Eq">Eq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-EqEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-EqEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.EqEq.html" class="struct"
title="struct syn::token::EqEq">EqEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Extern" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Extern" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Extern.html" class="struct"
title="struct syn::token::Extern">Extern</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-FatArrow" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-FatArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.FatArrow.html" class="struct"
title="struct syn::token::FatArrow">FatArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Final" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Final" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Final.html" class="struct"
title="struct syn::token::Final">Final</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Fn" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Fn" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Fn.html" class="struct"
title="struct syn::token::Fn">Fn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-For" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-For" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.For.html" class="struct"
title="struct syn::token::For">For</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ge" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Ge" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Ge.html" class="struct"
title="struct syn::token::Ge">Ge</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Gt" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Gt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Gt.html" class="struct"
title="struct syn::token::Gt">Gt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-If" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-If" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.If.html" class="struct"
title="struct syn::token::If">If</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Impl" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Impl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Impl.html" class="struct"
title="struct syn::token::Impl">Impl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-In" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-In" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.In.html" class="struct"
title="struct syn::token::In">In</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-LArrow" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-LArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.LArrow.html" class="struct"
title="struct syn::token::LArrow">LArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Le" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Le" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Le.html" class="struct"
title="struct syn::token::Le">Le</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Let" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Let" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Let.html" class="struct"
title="struct syn::token::Let">Let</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Loop" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Loop" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Loop.html" class="struct"
title="struct syn::token::Loop">Loop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Lt" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Lt" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Lt.html" class="struct"
title="struct syn::token::Lt">Lt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Macro-1" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Macro-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for syn::token::<a href="../token/struct.Macro.html" class="struct"
title="struct syn::token::Macro">Macro</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Match" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Match" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Match.html" class="struct"
title="struct syn::token::Match">Match</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Minus" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Minus" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Minus.html" class="struct"
title="struct syn::token::Minus">Minus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-MinusEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-MinusEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.MinusEq.html" class="struct"
title="struct syn::token::MinusEq">MinusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Mod" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Mod" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Mod.html" class="struct"
title="struct syn::token::Mod">Mod</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Move" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Move" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Move.html" class="struct"
title="struct syn::token::Move">Move</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Mut" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Mut" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Mut.html" class="struct"
title="struct syn::token::Mut">Mut</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ne" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Ne" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Ne.html" class="struct"
title="struct syn::token::Ne">Ne</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Not" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Not" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Not.html" class="struct"
title="struct syn::token::Not">Not</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Or" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Or" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Or.html" class="struct"
title="struct syn::token::Or">Or</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-OrEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-OrEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.OrEq.html" class="struct"
title="struct syn::token::OrEq">OrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-OrOr" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-OrOr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.OrOr.html" class="struct"
title="struct syn::token::OrOr">OrOr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Override" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Override" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Override.html" class="struct"
title="struct syn::token::Override">Override</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PathSep" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-PathSep" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.PathSep.html" class="struct"
title="struct syn::token::PathSep">PathSep</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Percent" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Percent" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Percent.html" class="struct"
title="struct syn::token::Percent">Percent</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PercentEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-PercentEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.PercentEq.html" class="struct"
title="struct syn::token::PercentEq">PercentEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Plus" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Plus" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Plus.html" class="struct"
title="struct syn::token::Plus">Plus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-PlusEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-PlusEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.PlusEq.html" class="struct"
title="struct syn::token::PlusEq">PlusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Pound" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Pound" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Pound.html" class="struct"
title="struct syn::token::Pound">Pound</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Priv" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Priv" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Priv.html" class="struct"
title="struct syn::token::Priv">Priv</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Pub" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Pub" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Pub.html" class="struct"
title="struct syn::token::Pub">Pub</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Question" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Question" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Question.html" class="struct"
title="struct syn::token::Question">Question</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-RArrow" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-RArrow" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.RArrow.html" class="struct"
title="struct syn::token::RArrow">RArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Raw" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Raw" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Raw.html" class="struct"
title="struct syn::token::Raw">Raw</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Ref" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Ref" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Ref.html" class="struct"
title="struct syn::token::Ref">Ref</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Return" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Return" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Return.html" class="struct"
title="struct syn::token::Return">Return</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SelfType" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-SelfType" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.SelfType.html" class="struct"
title="struct syn::token::SelfType">SelfType</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SelfValue" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-SelfValue" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.SelfValue.html" class="struct"
title="struct syn::token::SelfValue">SelfValue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Semi" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Semi" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Semi.html" class="struct"
title="struct syn::token::Semi">Semi</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Shl" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Shl" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Shl.html" class="struct"
title="struct syn::token::Shl">Shl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-ShlEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-ShlEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.ShlEq.html" class="struct"
title="struct syn::token::ShlEq">ShlEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Shr" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Shr" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Shr.html" class="struct"
title="struct syn::token::Shr">Shr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-ShrEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-ShrEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.ShrEq.html" class="struct"
title="struct syn::token::ShrEq">ShrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Slash" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Slash" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Slash.html" class="struct"
title="struct syn::token::Slash">Slash</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-SlashEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-SlashEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.SlashEq.html" class="struct"
title="struct syn::token::SlashEq">SlashEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Star" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Star" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Star.html" class="struct"
title="struct syn::token::Star">Star</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-StarEq" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-StarEq" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.StarEq.html" class="struct"
title="struct syn::token::StarEq">StarEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Static" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Static" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Static.html" class="struct"
title="struct syn::token::Static">Static</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Struct" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Struct" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Struct.html" class="struct"
title="struct syn::token::Struct">Struct</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Super" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Super" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Super.html" class="struct"
title="struct syn::token::Super">Super</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Tilde" class="section impl">

<a href="../../src/syn/token.rs.html#748-795"
class="src rightside">Source</a><a href="#impl-Parse-for-Tilde" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Tilde.html" class="struct"
title="struct syn::token::Tilde">Tilde</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Trait" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Trait" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Trait.html" class="struct"
title="struct syn::token::Trait">Trait</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Try" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Try" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Try.html" class="struct"
title="struct syn::token::Try">Try</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Type-1" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Type-1" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for syn::token::<a href="../token/struct.Type.html" class="struct"
title="struct syn::token::Type">Type</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Typeof" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Typeof" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Typeof.html" class="struct"
title="struct syn::token::Typeof">Typeof</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Underscore" class="section impl">

<a href="../../src/syn/token.rs.html#535-551"
class="src rightside">Source</a><a href="#impl-Parse-for-Underscore" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Underscore.html" class="struct"
title="struct syn::token::Underscore">Underscore</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Union" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Union" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Union.html" class="struct"
title="struct syn::token::Union">Union</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Unsafe" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Unsafe" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Unsafe.html" class="struct"
title="struct syn::token::Unsafe">Unsafe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Unsized" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Unsized" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Unsized.html" class="struct"
title="struct syn::token::Unsized">Unsized</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Use" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Use" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Use.html" class="struct"
title="struct syn::token::Use">Use</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Virtual" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Virtual" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Virtual.html" class="struct"
title="struct syn::token::Virtual">Virtual</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Where" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Where" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Where.html" class="struct"
title="struct syn::token::Where">Where</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-While" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-While" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.While.html" class="struct"
title="struct syn::token::While">While</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Yield" class="section impl">

<a href="../../src/syn/token.rs.html#692-746"
class="src rightside">Source</a><a href="#impl-Parse-for-Yield" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="../token/struct.Yield.html" class="struct"
title="struct syn::token::Yield">Yield</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Parse-for-Nothing" class="section impl">

<a href="../../src/syn/parse.rs.html#1370-1374"
class="src rightside">Source</a><a href="#impl-Parse-for-Nothing" class="anchor">§</a>

### impl <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a> for <a href="struct.Nothing.html" class="struct"
title="struct syn::parse::Nothing">Nothing</a>

</div>

</div>

</div>

</div>
