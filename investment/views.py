from django.http import Http404
from django.shortcuts import render

from .content import (
    ASSET_CATEGORIES,
    ASSET_ORDER,
    CATEGORY_STEPS,
    COMMON_QUESTIONS,
    PURCHASE_STEPS,
    PRODUCT_EXPLANATIONS,
    PRODUCT_LINKS,
)


def _ordered_categories():
    return [ASSET_CATEGORIES[key] for key in ASSET_ORDER]


def _category_by_slug(slug):
    for category in ASSET_CATEGORIES.values():
        if slug in (category["slug"], category["legacy_slug"]):
            return category
    raise Http404("Asset category not found")


def index(request):
    return render(
        request,
        "investment/index.html",
        {
            "categories": list(reversed(_ordered_categories())),
            "questions": COMMON_QUESTIONS,
        },
    )


def category(request, category_slug):
    asset_category = _category_by_slug(category_slug)
    return render(
        request,
        "investment/detail.html",
        {
            "category": asset_category,
            "purchase_steps": PURCHASE_STEPS[asset_category["slug"]],
            "base_steps": CATEGORY_STEPS,
            "other_categories": [
                item for item in _ordered_categories() if item is not asset_category
            ],
        },
    )


def asset_detail(request, category_slug, asset_slug):
    asset_category = _category_by_slug(category_slug)
    asset = next(
        (
            item
            for item in asset_category["subcategories"]
            if item["slug"] == asset_slug
        ),
        None,
    )
    if asset is None:
        raise Http404("Asset detail not found")

    product_names = asset["etfs"] or asset["representatives"]
    product_rows = [
        {
            "name": product,
            "description": PRODUCT_EXPLANATIONS.get(product, ""),
            "link": PRODUCT_LINKS.get(product, ""),
        }
        for product in product_names
    ]
    product_rows.extend(
        {
            "name": product,
            "description": PRODUCT_EXPLANATIONS.get(
                product,
                "",
            ),
            "link": PRODUCT_LINKS.get(product, ""),
        }
        for product in asset["funds"]
    )
    official_links = [{"label": label, "url": url} for label, url in asset["links"]]
    has_product_links = any(product["link"] for product in product_rows)
    attention_items = [asset["risk"], *asset["limits"]]
    if asset_category["slug"] == "etf-fund":
        attention_items.extend(
            [
                "ETF分散的是单一公司的风险，不能避免整个市场下跌。宽基指数在市场回调时同样可能出现明显亏损。",
                "查看成交量和买卖价差。交易冷清的ETF可能难以及时成交，实际买入价和卖出价也可能相差较大。",
                "比较市场价格与基金净值。交易价格明显高于净值时属于溢价，追高买入后可能因溢价收窄产生额外损失。",
                "同时比较基金规模、管理费、跟踪误差和存续情况。规模过小的产品可能面临合并或终止风险。",
                "检查持仓重叠。全球基金、美国基金和科技主题基金可能同时重仓相同大型公司，并不一定形成真正分散。",
                "ETF可以长期持有，也可以短期交易；频繁操作会增加交易成本，并提高受短期情绪影响的概率。",
            ]
        )

    return render(
        request,
        "investment/asset_detail.html",
        {
            "category": asset_category,
            "asset": asset,
            "example_title": asset.get("example_title", "产品示例"),
            "example_name_label": asset.get("example_name_label", "产品名称"),
            "product_rows": product_rows,
            "has_product_links": has_product_links,
            "official_links": official_links,
            "attention_items": attention_items,
            "purchase_steps": PURCHASE_STEPS[asset_category["slug"]],
        },
    )


def cash(request):
    return category(request, "cash-deposit")


def etf(request):
    return category(request, "etf-fund")


def reit(request):
    return category(request, "reit-gold")


def stocks(request):
    return category(request, "stocks")


def crypto(request):
    return category(request, "crypto")
