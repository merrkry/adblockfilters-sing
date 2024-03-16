# adblockfilters-sing

将来自 [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) 的去广告规则转化为 sing-box 的 [rule-set](https://sing-box.sagernet.org/zh/configuration/rule-set/source-format/)。

通过 Github Actions 自动打包，每天执行一次。

[订阅地址](http://raw.githubusercontent.com/merrkry/adblockfilters-sing/main/adblockfilters-sing.srs)（请自行准备 ghproxy 或通过代理/公共 CDN 拉取）

注意：sing-box 文档中提到「引用的规则集可视为被**合并**，而不是作为一个单独的规则子项」。由于本规则集通过逻辑规则实现了原规则中的白名单，强烈建议为本规则集单独添加规则，或置于逻辑规则中，以确保匹配逻辑正常。
