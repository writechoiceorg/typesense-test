import typesense

client = typesense.Client({
    'nodes': [{
        'host': 'zjsxp3nl1oqih2vep-1.a1.typesense.net',  # For Typesense Cloud use xxx.a1.typesense.net
        'port': '443',       # For Typesense Cloud use 443
        'protocol': 'https'    # For Typesense Cloud use https
    }],
    'api_key': '2tOW7InWQ4wB18ZrG1c8a8NfT72G3Wx8',
    'connection_timeout_seconds': 2
})

combined_schema = {
    "name": "new_combined_collection",
    "fields": [
        {"name": "term_id", "type": "string", "facet": False, "optional": True},
        {"name": "taxonomy", "type": "string", "facet": False, "optional": True},
        {"name": "post_title", "type": "string", "facet": False, "optional": True},
        {"name": "post_content", "type": "string", "facet": False, "optional": True},
        {"name": "slug", "type": "string", "facet": False, "optional": True},
        {"name": "posts_count", "type": "int64", "facet": False, "optional": True, "sort": True},
        {"name": "permalink", "type": "string", "facet": False, "optional": True},
        {"name": "post_type", "type": "string", "facet": False, "optional": True},
        {"name": "post_author", "type": "string", "facet": False, "optional": True},
        {"name": "comment_count", "type": "int64", "facet": False, "optional": True, "sort": True},
        {"name": "is_sticky", "type": "int32", "facet": False, "optional": True, "sort": True},
        {"name": "post_excerpt", "type": "string", "facet": False, "optional": True},
        {"name": "post_date", "type": "string", "facet": False, "optional": True},
        {"name": "sort_by_date", "type": "int64", "facet": False, "optional": True, "sort": True},
        {"name": "post_id", "type": "string", "facet": False, "optional": True},
        {"name": "post_modified", "type": "string", "facet": False, "optional": True},
        {"name": "post_thumbnail", "type": "string", "facet": False, "optional": True},
        {"name": "post_thumbnail_html", "type": "string", "facet": False, "optional": True},
        {"name": "category", "type": "string[]", "facet": True, "optional": True},
        {"name": "cat_link", "type": "string[]", "facet": False, "optional": True},
        {"name": "tags", "type": "string[]", "facet": True, "optional": True},
        {"name": "tag_links", "type": "string[]", "facet": False, "optional": True},
        {"name": "anchor", "type": "string", "facet": False, "optional": True},
        {"name": "content", "type": "string", "facet": False, "optional": True},
        {"name": "url", "type": "string", "facet": True, "optional": False},
        {"name": "url_without_anchor", "type": "string", "facet": True, "optional": True},
        {"name": "version", "type": "string[]", "facet": True, "optional": True},
        {"name": "hierarchy.lvl0", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl1", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl2", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl3", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl4", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl5", "type": "string", "facet": True, "optional": True},
        {"name": "hierarchy.lvl6", "type": "string", "facet": True, "optional": True},
        {"name": "type", "type": "string", "facet": True, "optional": True},
        {"name": ".*_tag", "type": "string", "facet": True, "optional": True},
        {"name": "language", "type": "string", "facet": True, "optional": True},
        {"name": "docusaurus_tag", "type": "string", "facet": True, "optional": True},
        {"name": "item_priority", "type": "int64", "facet": False, "optional": False, "sort": True}
    ],
    "default_sorting_field": "item_priority"
}

client.collections.create(combined_schema)
