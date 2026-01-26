<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[token](index.html)

</div>

# Trait <span class="trait">Token</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/token.rs.html#125-133"
class="src">Source</a> </span>

</div>

``` rust
pub trait Token: Sealed { }
```

Expand description

<div class="docblock">

Marker trait for types that represent single tokens.

This trait is sealed and cannot be implemented for types outside of Syn.

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-Token-for-TokenTree" class="section impl">

<a href="../../src/verus_syn/token.rs.html#183"
class="src rightside">Source</a><a href="#impl-Token-for-TokenTree" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Group" class="section impl">

<a href="../../src/verus_syn/token.rs.html#184"
class="src rightside">Source</a><a href="#impl-Token-for-Group" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../../proc_macro2/struct.Group.html" class="struct"
title="struct proc_macro2::Group">Group</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Literal" class="section impl">

<a href="../../src/verus_syn/token.rs.html#182"
class="src rightside">Source</a><a href="#impl-Token-for-Literal" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../../proc_macro2/struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Punct" class="section impl">

<a href="../../src/verus_syn/token.rs.html#181"
class="src rightside">Source</a><a href="#impl-Token-for-Punct" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../../proc_macro2/struct.Punct.html" class="struct"
title="struct proc_macro2::Punct">Punct</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Token-for-Lit" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1057"
class="src rightside">Source</a><a href="#impl-Token-for-Lit" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../enum.Lit.html" class="enum"
title="enum verus_syn::Lit">Lit</a>

</div>

<div id="impl-Token-for-Ident" class="section impl">

<a href="../../src/verus_syn/ident.rs.html#95-107"
class="src rightside">Source</a><a href="#impl-Token-for-Ident" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Token-for-Lifetime" class="section impl">

<a href="../../src/verus_syn/token.rs.html#185"
class="src rightside">Source</a><a href="#impl-Token-for-Lifetime" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-LitBool" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1065"
class="src rightside">Source</a><a href="#impl-Token-for-LitBool" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitBool.html" class="struct"
title="struct verus_syn::LitBool">LitBool</a>

</div>

<div id="impl-Token-for-LitByte" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1061"
class="src rightside">Source</a><a href="#impl-Token-for-LitByte" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitByte.html" class="struct"
title="struct verus_syn::LitByte">LitByte</a>

</div>

<div id="impl-Token-for-LitByteStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1059"
class="src rightside">Source</a><a href="#impl-Token-for-LitByteStr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitByteStr.html" class="struct"
title="struct verus_syn::LitByteStr">LitByteStr</a>

</div>

<div id="impl-Token-for-LitCStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1060"
class="src rightside">Source</a><a href="#impl-Token-for-LitCStr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitCStr.html" class="struct"
title="struct verus_syn::LitCStr">LitCStr</a>

</div>

<div id="impl-Token-for-LitChar" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1062"
class="src rightside">Source</a><a href="#impl-Token-for-LitChar" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitChar.html" class="struct"
title="struct verus_syn::LitChar">LitChar</a>

</div>

<div id="impl-Token-for-LitFloat" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1064"
class="src rightside">Source</a><a href="#impl-Token-for-LitFloat" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitFloat.html" class="struct"
title="struct verus_syn::LitFloat">LitFloat</a>

</div>

<div id="impl-Token-for-LitInt" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1063"
class="src rightside">Source</a><a href="#impl-Token-for-LitInt" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitInt.html" class="struct"
title="struct verus_syn::LitInt">LitInt</a>

</div>

<div id="impl-Token-for-LitStr" class="section impl">

<a href="../../src/verus_syn/lit.rs.html#1058"
class="src rightside">Source</a><a href="#impl-Token-for-LitStr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="../struct.LitStr.html" class="struct"
title="struct verus_syn::LitStr">LitStr</a>

</div>

<div id="impl-Token-for-Abstract" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Abstract" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Abstract.html" class="struct"
title="struct verus_syn::token::Abstract">Abstract</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-And" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-And" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.And.html" class="struct"
title="struct verus_syn::token::And">And</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-AndAnd" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-AndAnd" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.AndAnd.html" class="struct"
title="struct verus_syn::token::AndAnd">AndAnd</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-AndEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-AndEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.AndEq.html" class="struct"
title="struct verus_syn::token::AndEq">AndEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-As" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-As" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.As.html" class="struct"
title="struct verus_syn::token::As">As</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Assert" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Assert" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Assert.html" class="struct"
title="struct verus_syn::token::Assert">Assert</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Assume" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Assume" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Assume.html" class="struct"
title="struct verus_syn::token::Assume">Assume</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-AssumeSpecification" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-AssumeSpecification" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::token::AssumeSpecification">AssumeSpecification</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Async" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Async" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Async.html" class="struct"
title="struct verus_syn::token::Async">Async</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-At" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-At" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.At.html" class="struct"
title="struct verus_syn::token::At">At</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Auto" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Auto" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Auto.html" class="struct"
title="struct verus_syn::token::Auto">Auto</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Await" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Await" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Await.html" class="struct"
title="struct verus_syn::token::Await">Await</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Axiom" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Axiom" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Axiom.html" class="struct"
title="struct verus_syn::token::Axiom">Axiom</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Become" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Become" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Become.html" class="struct"
title="struct verus_syn::token::Become">Become</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-BigAnd" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-BigAnd" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.BigAnd.html" class="struct"
title="struct verus_syn::token::BigAnd">BigAnd</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-BigOr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-BigOr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.BigOr.html" class="struct"
title="struct verus_syn::token::BigOr">BigOr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Box" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Box" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Box.html" class="struct"
title="struct verus_syn::token::Box">Box</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Brace" class="section impl">

<a href="../../src/verus_syn/token.rs.html#660-668"
class="src rightside">Source</a><a href="#impl-Token-for-Brace" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Brace.html" class="struct"
title="struct verus_syn::token::Brace">Brace</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Bracket" class="section impl">

<a href="../../src/verus_syn/token.rs.html#671-679"
class="src rightside">Source</a><a href="#impl-Token-for-Bracket" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Bracket.html" class="struct"
title="struct verus_syn::token::Bracket">Bracket</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Break" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Break" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Break.html" class="struct"
title="struct verus_syn::token::Break">Break</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Broadcast" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Broadcast" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Broadcast.html" class="struct"
title="struct verus_syn::token::Broadcast">Broadcast</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-BroadcastGroup" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-BroadcastGroup" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.BroadcastGroup.html" class="struct"
title="struct verus_syn::token::BroadcastGroup">BroadcastGroup</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-By" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-By" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.By.html" class="struct"
title="struct verus_syn::token::By">By</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Caret" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Caret" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Caret.html" class="struct"
title="struct verus_syn::token::Caret">Caret</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-CaretEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-CaretEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.CaretEq.html" class="struct"
title="struct verus_syn::token::CaretEq">CaretEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Choose" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Choose" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Choose.html" class="struct"
title="struct verus_syn::token::Choose">Choose</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Closed" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Closed" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Closed.html" class="struct"
title="struct verus_syn::token::Closed">Closed</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Colon" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Colon" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Colon.html" class="struct"
title="struct verus_syn::token::Colon">Colon</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Comma" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Comma" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Comma.html" class="struct"
title="struct verus_syn::token::Comma">Comma</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Const" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Const" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Const.html" class="struct"
title="struct verus_syn::token::Const">Const</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Continue" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Continue" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Continue.html" class="struct"
title="struct verus_syn::token::Continue">Continue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Crate" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Crate" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Crate.html" class="struct"
title="struct verus_syn::token::Crate">Crate</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Decreases" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Decreases" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Decreases.html" class="struct"
title="struct verus_syn::token::Decreases">Decreases</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Default" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Default" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Default.html" class="struct"
title="struct verus_syn::token::Default">Default</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-DefaultEnsures" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-DefaultEnsures" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::token::DefaultEnsures">DefaultEnsures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Do" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Do" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Do.html" class="struct"
title="struct verus_syn::token::Do">Do</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Dollar" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Dollar" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Dollar.html" class="struct"
title="struct verus_syn::token::Dollar">Dollar</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Dot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Dot" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Dot.html" class="struct"
title="struct verus_syn::token::Dot">Dot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-DotDot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-DotDot" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.DotDot.html" class="struct"
title="struct verus_syn::token::DotDot">DotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-DotDotDot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-DotDotDot" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.DotDotDot.html" class="struct"
title="struct verus_syn::token::DotDotDot">DotDotDot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-DotDotEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-DotDotEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.DotDotEq.html" class="struct"
title="struct verus_syn::token::DotDotEq">DotDotEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Dyn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Dyn" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Dyn.html" class="struct"
title="struct verus_syn::token::Dyn">Dyn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Else" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Else" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Else.html" class="struct"
title="struct verus_syn::token::Else">Else</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Ensures" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Ensures" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ensures.html" class="struct"
title="struct verus_syn::token::Ensures">Ensures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Enum" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Enum" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Enum.html" class="struct"
title="struct verus_syn::token::Enum">Enum</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Eq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Eq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Eq.html" class="struct"
title="struct verus_syn::token::Eq">Eq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-EqEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-EqEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.EqEq.html" class="struct"
title="struct verus_syn::token::EqEq">EqEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-EqEqEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-EqEqEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.EqEqEq.html" class="struct"
title="struct verus_syn::token::EqEqEq">EqEqEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Equiv" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Equiv" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Equiv.html" class="struct"
title="struct verus_syn::token::Equiv">Equiv</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Exec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Exec" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Exec.html" class="struct"
title="struct verus_syn::token::Exec">Exec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Exists" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Exists" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Exists.html" class="struct"
title="struct verus_syn::token::Exists">Exists</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Exply" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Exply" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Exply.html" class="struct"
title="struct verus_syn::token::Exply">Exply</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Extern" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Extern" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Extern.html" class="struct"
title="struct verus_syn::token::Extern">Extern</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-FatArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-FatArrow" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.FatArrow.html" class="struct"
title="struct verus_syn::token::FatArrow">FatArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Final" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Final" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Final.html" class="struct"
title="struct verus_syn::token::Final">Final</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Fn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Fn" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Fn.html" class="struct"
title="struct verus_syn::token::Fn">Fn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-FnSpec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-FnSpec" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.FnSpec.html" class="struct"
title="struct verus_syn::token::FnSpec">FnSpec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-For" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-For" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.For.html" class="struct"
title="struct verus_syn::token::For">For</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Forall" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Forall" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Forall.html" class="struct"
title="struct verus_syn::token::Forall">Forall</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Ge" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Ge" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ge.html" class="struct"
title="struct verus_syn::token::Ge">Ge</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Ghost" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Ghost" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ghost.html" class="struct"
title="struct verus_syn::token::Ghost">Ghost</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Global" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Global" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Global.html" class="struct"
title="struct verus_syn::token::Global">Global</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Group-1" class="section impl">

<a href="../../src/verus_syn/token.rs.html#682-690"
class="src rightside">Source</a><a href="#impl-Token-for-Group-1" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for verus_syn::token::<a href="struct.Group.html" class="struct"
title="struct verus_syn::token::Group">Group</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Gt" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Gt" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Gt.html" class="struct"
title="struct verus_syn::token::Gt">Gt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Has" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Has" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Has.html" class="struct"
title="struct verus_syn::token::Has">Has</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-HasNot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-HasNot" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.HasNot.html" class="struct"
title="struct verus_syn::token::HasNot">HasNot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Hide" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Hide" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Hide.html" class="struct"
title="struct verus_syn::token::Hide">Hide</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-If" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-If" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.If.html" class="struct"
title="struct verus_syn::token::If">If</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Impl" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Impl" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Impl.html" class="struct"
title="struct verus_syn::token::Impl">Impl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Implies" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Implies" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Implies.html" class="struct"
title="struct verus_syn::token::Implies">Implies</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Imply" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Imply" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Imply.html" class="struct"
title="struct verus_syn::token::Imply">Imply</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-In" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-In" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.In.html" class="struct"
title="struct verus_syn::token::In">In</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-InvAny" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-InvAny" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.InvAny.html" class="struct"
title="struct verus_syn::token::InvAny">InvAny</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-InvNone" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-InvNone" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.InvNone.html" class="struct"
title="struct verus_syn::token::InvNone">InvNone</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Invariant" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Invariant" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Invariant.html" class="struct"
title="struct verus_syn::token::Invariant">Invariant</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-InvariantEnsures" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-InvariantEnsures" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::token::InvariantEnsures">InvariantEnsures</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-InvariantExceptBreak" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-InvariantExceptBreak" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::token::InvariantExceptBreak">InvariantExceptBreak</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Is" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Is" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Is.html" class="struct"
title="struct verus_syn::token::Is">Is</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-IsNot" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-IsNot" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.IsNot.html" class="struct"
title="struct verus_syn::token::IsNot">IsNot</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-LArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-LArrow" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.LArrow.html" class="struct"
title="struct verus_syn::token::LArrow">LArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Layout" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Layout" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Layout.html" class="struct"
title="struct verus_syn::token::Layout">Layout</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Le" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Le" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Le.html" class="struct"
title="struct verus_syn::token::Le">Le</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Let" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Let" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Let.html" class="struct"
title="struct verus_syn::token::Let">Let</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Loop" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Loop" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Loop.html" class="struct"
title="struct verus_syn::token::Loop">Loop</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Lt" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Lt" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Lt.html" class="struct"
title="struct verus_syn::token::Lt">Lt</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Macro" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Macro" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Macro.html" class="struct"
title="struct verus_syn::token::Macro">Macro</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Match" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Match" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Match.html" class="struct"
title="struct verus_syn::token::Match">Match</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Matches" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Matches" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Matches.html" class="struct"
title="struct verus_syn::token::Matches">Matches</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Minus" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Minus" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Minus.html" class="struct"
title="struct verus_syn::token::Minus">Minus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-MinusEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-MinusEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.MinusEq.html" class="struct"
title="struct verus_syn::token::MinusEq">MinusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Mod" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Mod" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Mod.html" class="struct"
title="struct verus_syn::token::Mod">Mod</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Move" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Move" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Move.html" class="struct"
title="struct verus_syn::token::Move">Move</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Mut" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Mut" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Mut.html" class="struct"
title="struct verus_syn::token::Mut">Mut</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Ne" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Ne" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ne.html" class="struct"
title="struct verus_syn::token::Ne">Ne</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-NeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-NeEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.NeEq.html" class="struct"
title="struct verus_syn::token::NeEq">NeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-NoUnwind" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-NoUnwind" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.NoUnwind.html" class="struct"
title="struct verus_syn::token::NoUnwind">NoUnwind</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Not" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Not" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Not.html" class="struct"
title="struct verus_syn::token::Not">Not</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Open" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Open" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Open.html" class="struct"
title="struct verus_syn::token::Open">Open</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-OpensInvariants" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-OpensInvariants" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.OpensInvariants.html" class="struct"
title="struct verus_syn::token::OpensInvariants">OpensInvariants</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Or" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Or" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Or.html" class="struct"
title="struct verus_syn::token::Or">Or</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-OrEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-OrEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.OrEq.html" class="struct"
title="struct verus_syn::token::OrEq">OrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-OrOr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-OrOr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.OrOr.html" class="struct"
title="struct verus_syn::token::OrOr">OrOr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Override" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Override" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Override.html" class="struct"
title="struct verus_syn::token::Override">Override</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Paren" class="section impl">

<a href="../../src/verus_syn/token.rs.html#649-657"
class="src rightside">Source</a><a href="#impl-Token-for-Paren" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Paren.html" class="struct"
title="struct verus_syn::token::Paren">Paren</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-PathSep" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-PathSep" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.PathSep.html" class="struct"
title="struct verus_syn::token::PathSep">PathSep</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Percent" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Percent" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Percent.html" class="struct"
title="struct verus_syn::token::Percent">Percent</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-PercentEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-PercentEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.PercentEq.html" class="struct"
title="struct verus_syn::token::PercentEq">PercentEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Plus" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Plus" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Plus.html" class="struct"
title="struct verus_syn::token::Plus">Plus</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-PlusEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-PlusEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.PlusEq.html" class="struct"
title="struct verus_syn::token::PlusEq">PlusEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Pound" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Pound" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Pound.html" class="struct"
title="struct verus_syn::token::Pound">Pound</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Priv" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Priv" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Priv.html" class="struct"
title="struct verus_syn::token::Priv">Priv</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Proof" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Proof" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Proof.html" class="struct"
title="struct verus_syn::token::Proof">Proof</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-ProofFn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-ProofFn" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.ProofFn.html" class="struct"
title="struct verus_syn::token::ProofFn">ProofFn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Pub" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Pub" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Pub.html" class="struct"
title="struct verus_syn::token::Pub">Pub</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Question" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Question" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Question.html" class="struct"
title="struct verus_syn::token::Question">Question</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-RArrow" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-RArrow" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.RArrow.html" class="struct"
title="struct verus_syn::token::RArrow">RArrow</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Raw" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Raw" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Raw.html" class="struct"
title="struct verus_syn::token::Raw">Raw</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Recommends" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Recommends" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Recommends.html" class="struct"
title="struct verus_syn::token::Recommends">Recommends</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Ref" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Ref" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ref.html" class="struct"
title="struct verus_syn::token::Ref">Ref</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Requires" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Requires" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Requires.html" class="struct"
title="struct verus_syn::token::Requires">Requires</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Return" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Return" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Return.html" class="struct"
title="struct verus_syn::token::Return">Return</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Returns" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Returns" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Returns.html" class="struct"
title="struct verus_syn::token::Returns">Returns</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Reveal" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Reveal" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Reveal.html" class="struct"
title="struct verus_syn::token::Reveal">Reveal</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-RevealWithFuel" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-RevealWithFuel" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.RevealWithFuel.html" class="struct"
title="struct verus_syn::token::RevealWithFuel">RevealWithFuel</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-SelfType" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-SelfType" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.SelfType.html" class="struct"
title="struct verus_syn::token::SelfType">SelfType</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-SelfValue" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-SelfValue" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.SelfValue.html" class="struct"
title="struct verus_syn::token::SelfValue">SelfValue</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Semi" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Semi" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Semi.html" class="struct"
title="struct verus_syn::token::Semi">Semi</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Shl" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Shl" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Shl.html" class="struct"
title="struct verus_syn::token::Shl">Shl</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-ShlEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-ShlEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.ShlEq.html" class="struct"
title="struct verus_syn::token::ShlEq">ShlEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Shr" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Shr" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Shr.html" class="struct"
title="struct verus_syn::token::Shr">Shr</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-ShrEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-ShrEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.ShrEq.html" class="struct"
title="struct verus_syn::token::ShrEq">ShrEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-SizeOf" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-SizeOf" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.SizeOf.html" class="struct"
title="struct verus_syn::token::SizeOf">SizeOf</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Slash" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Slash" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Slash.html" class="struct"
title="struct verus_syn::token::Slash">Slash</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-SlashEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-SlashEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.SlashEq.html" class="struct"
title="struct verus_syn::token::SlashEq">SlashEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Spec" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Spec" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Spec.html" class="struct"
title="struct verus_syn::token::Spec">Spec</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-SpecFn" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-SpecFn" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.SpecFn.html" class="struct"
title="struct verus_syn::token::SpecFn">SpecFn</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Star" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Star" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Star.html" class="struct"
title="struct verus_syn::token::Star">Star</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-StarEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-StarEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.StarEq.html" class="struct"
title="struct verus_syn::token::StarEq">StarEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Static" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Static" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Static.html" class="struct"
title="struct verus_syn::token::Static">Static</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Struct" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Struct" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Struct.html" class="struct"
title="struct verus_syn::token::Struct">Struct</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Super" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Super" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Super.html" class="struct"
title="struct verus_syn::token::Super">Super</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Tilde" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-Tilde" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Tilde.html" class="struct"
title="struct verus_syn::token::Tilde">Tilde</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-TildeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-TildeEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.TildeEq.html" class="struct"
title="struct verus_syn::token::TildeEq">TildeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-TildeNe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-TildeNe" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.TildeNe.html" class="struct"
title="struct verus_syn::token::TildeNe">TildeNe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-TildeTildeEq" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-TildeTildeEq" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.TildeTildeEq.html" class="struct"
title="struct verus_syn::token::TildeTildeEq">TildeTildeEq</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-TildeTildeNe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#799-859"
class="src rightside">Source</a><a href="#impl-Token-for-TildeTildeNe" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.TildeTildeNe.html" class="struct"
title="struct verus_syn::token::TildeTildeNe">TildeTildeNe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Tracked" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Tracked" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Tracked.html" class="struct"
title="struct verus_syn::token::Tracked">Tracked</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Trait" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Trait" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Trait.html" class="struct"
title="struct verus_syn::token::Trait">Trait</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Try" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Try" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Try.html" class="struct"
title="struct verus_syn::token::Try">Try</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Type" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Type" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Type.html" class="struct"
title="struct verus_syn::token::Type">Type</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Typeof" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Typeof" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Typeof.html" class="struct"
title="struct verus_syn::token::Typeof">Typeof</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Underscore" class="section impl">

<a href="../../src/verus_syn/token.rs.html#554-568"
class="src rightside">Source</a><a href="#impl-Token-for-Underscore" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Underscore.html" class="struct"
title="struct verus_syn::token::Underscore">Underscore</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Uninterp" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Uninterp" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Uninterp.html" class="struct"
title="struct verus_syn::token::Uninterp">Uninterp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Union" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Union" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Union.html" class="struct"
title="struct verus_syn::token::Union">Union</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Unsafe" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Unsafe" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Unsafe.html" class="struct"
title="struct verus_syn::token::Unsafe">Unsafe</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Unsized" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Unsized" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Unsized.html" class="struct"
title="struct verus_syn::token::Unsized">Unsized</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Use" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Use" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Use.html" class="struct"
title="struct verus_syn::token::Use">Use</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Via" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Via" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Via.html" class="struct"
title="struct verus_syn::token::Via">Via</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Virtual" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Virtual" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Virtual.html" class="struct"
title="struct verus_syn::token::Virtual">Virtual</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-When" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-When" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.When.html" class="struct"
title="struct verus_syn::token::When">When</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Where" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Where" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Where.html" class="struct"
title="struct verus_syn::token::Where">Where</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-While" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-While" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.While.html" class="struct"
title="struct verus_syn::token::While">While</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-With" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-With" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.With.html" class="struct"
title="struct verus_syn::token::With">With</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-Yield" class="section impl">

<a href="../../src/verus_syn/token.rs.html#692-797"
class="src rightside">Source</a><a href="#impl-Token-for-Yield" class="anchor">§</a>

### impl <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Yield.html" class="struct"
title="struct verus_syn::token::Yield">Yield</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Token-for-T" class="section impl">

<a href="../../src/verus_syn/token.rs.html#191-199"
class="src rightside">Source</a><a href="#impl-Token-for-T" class="anchor">§</a>

### impl\<T: CustomToken\> <a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for T

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

</div>

</div>

</div>
