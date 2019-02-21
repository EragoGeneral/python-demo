class Balance:
    def __init__(self, created_at, net_value, prev_net_value, prev_price, prev_target_volume, prev_target_weight, prev_volume, prev_weight, prev_weight_adjusted, price, proactive, rebalancing_id, stock_id, stock_name, stock_symbol, target_volume, target_weight, updated_at, volume, weight):
        self.created_at = created_at
        self.net_value = net_value
        self.prev_net_value = prev_net_value
        self.prev_price = prev_price
        self.prev_target_volume = prev_target_volume
        self.prev_target_weight = prev_target_weight
        self.prev_volume = prev_volume
        self.prev_weight = prev_weight
        self.prev_weight_adjusted = prev_weight_adjusted
        self.price = price
        self.proactive = proactive
        self.rebalancing_id = rebalancing_id
        self.stock_id = stock_id
        self.stock_name = stock_name
        self.stock_symbol = stock_symbol
        self.target_volume = target_volume
        self.target_weight = target_weight
        self.updated_at = updated_at
        self.volume = volume
        self.weight = weight

    def get_stock_name(self):
        return self.stock_name

