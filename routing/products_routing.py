import logging
import psycopg2
import psycopg2.extras
import utils.error_messages as errors
import utils.valid_messages as valid_messages
import utils.tools as tools

from database.db_connection import sql_connection
from dateutil import parser
from flask import Blueprint


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = True


products_routing_blueprint = Blueprint("products_routing", __name__)


@products_routing_blueprint.route("/<string:manufacturer>", methods=["GET"])
def get_manufacturer(manufacturer):
    """
    Returns the products matching the manufacturer.

    :param manufacturer: identify the manufacturer
    :return: dictionary the products
    """
    if manufacturer != 'nvidia' and manufacturer != 'amd':
        logger.error(errors.PARAM_NOT_VALID)
        return {}

    query = f"""
                SELECT
                json_agg(json_build_object('name', p.name, 'price', p.price, 'url', p.url, 'image', p.image, 'shop', p.shop_name, 'last_update', p.updated_at)) AS products_data
                FROM products p
                WHERE p.brand = '{manufacturer}' AND p.updated_at >= NOW() - INTERVAL '3 days';
            """

    connection = sql_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    product_dict = dict(cursor.fetchone())
    connection.close()

    products = product_dict.get("products_data", [])
    for p in products:
      if p.get('last_update', False):
          dt = parser.isoparse(p["last_update"])
          p["last_update"] = tools.humanize_last_update(dt)

    valid_messages.petition_completed('products_routing')
    return product_dict

