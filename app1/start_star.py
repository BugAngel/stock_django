from app1.models import StockDailyBasic

def startStar(firstDate, secondDate, thirdDate, firstThreshold=0.5, thirdThreshold=0.6):
    print('进入:startStar')
    print('firstDate:'+firstDate)
    print('secondDate:' + secondDate)
    print('thirdDate:' + thirdDate)
    return StockDailyBasic.objects.raw("""
SELECT
    third.trade_date,
    first.ts_code,
    basic.symbol,
    basic.name,
    basic.industry,
    third.amount
FROM (
        -- 第一天  大阴线
        SELECT
            ts_code,
            close,
            low,
            vol
        FROM daily
        WHERE
            trade_date = %s
            AND open > close
            AND (open - close) / (high - low) > %s
    ) AS first
    JOIN (
        -- 第二天 实体较小,跳空开盘,收盘价小于昨天收盘价
        SELECT
            ts_code,
            open,
            close,
            vol
        FROM daily
        WHERE
            trade_date = %s
    ) AS second ON first.ts_code = second.ts_code
    JOIN (
        -- 第三天 大阳线,收盘价大于第一天收盘价
        SELECT
            ts_code,
            open,
            close,
            vol,
            amount,
            trade_date
        FROM daily
        WHERE
            trade_date = %s
            AND (close - open) / (high - low) > %s
    ) AS third ON first.ts_code = third.ts_code
    JOIN (
        SELECT
            ts_code,
            symbol,
            name,
            industry
        FROM
            stock_basic
        WHERE market = '主板'
    ) AS basic ON first.ts_code = basic.ts_code
WHERE
    second.open < first.low
    AND second.close < first.close
    AND third.close > first.close
    AND third.vol > second.vol
    AND third.vol > first.vol
ORDER BY third.amount DESC    
    """, [firstDate, firstThreshold, secondDate, thirdDate, thirdThreshold])
