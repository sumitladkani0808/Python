from lxml import etree

xml_string = """<?xml version="1.0"?>
<?xml-stylesheet href="catalog.xsl" type="text/xsl"?>
<!DOCTYPE catalog SYSTEM "catalog.dtd">
<catalog>
    <Header>
        <Version>100</Version>
    </Header>
    <product description="Cardigan Sweater" product_image="cardigan.jpg">
        <catalog_item gender="Men's">
            <item_number>QWZ5671</item_number>
            <price>39.95</price>
            <size description="Medium">
                <color_swatch image="red_cardigan.jpg">Red</color_swatch>
                <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
            </size>
            <size description="Large">
                <color_swatch image="red_cardigan.jpg">Red</color_swatch>
                <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
            </size>
        </catalog_item>
        <catalog_item gender="Women's">
            <item_number>RRX9856</item_number>
            <price>42.50</price>
            <size description="Small">
                <color_swatch image="red_cardigan.jpg">Red</color_swatch>
                <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
                <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
            </size>
            <size description="Medium">
                <color_swatch image="red_cardigan.jpg">Red</color_swatch>
                <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
                <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
                <color_swatch image="black_cardigan.jpg">Black</color_swatch>
            </size>
            <size description="Large">
                <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
                <color_swatch image="black_cardigan.jpg">Black</color_swatch>
            </size>
            <size description="Extra Large">
                <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
                <color_swatch image="black_cardigan.jpg">Black</color_swatch>
            </size>
        </catalog_item>
    </product>
</catalog>"""

# xpath_string = '/catalog/product[@description="Cardigan Sweater"]/catalog_item[2]/size[3]/color_swatch[2]@image'
xpath_string = '/catalog/Header/Version'
# xpath_string = '/catalog/product[@description="Cardigan Sweater"]/catalog_item[1]/item_number'
# xpath_string = '/catalog/product[@description="Cardigan Sweater"]/catalog_item[2]/size[4]//color_swatch[1]/text()'
# xpath_string = '/catalog/product[@description="Cardigan Sweater"]/catalog_item[2]/size[4]//color_swatch[2]/text()'
tree = etree.XML(xml_string)
if tree is not None:
    try:
        xpath_value_ref = tree.xpath(xpath_string)
        if not (hasattr(xpath_value_ref[0], 'text')):
            print('IN IF CONDITION')
            xpath_value = xpath_value_ref[0].strip()
        else:
            print('IN ELSE CONDITION')
            xpath_value = xpath_value_ref[0].text.strip()
        print('xpath_value is :- [{}]'.format(xpath_value))
    except Exception as e:
        print('Error while getting Xpath :- [{}]'.format(e.error_log))
