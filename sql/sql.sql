SELECT *
FROM (
# 查询移款单供应商与原付款单供应商ID
         SELECT sa.order_no            '移款单',
                sa.supplier_id         '移供ID',
                sa.payment_order_id    '原付ID',
                st.supplier_account_id '原供ID',
                st.is_tax              '原含税'

         FROM procurement_transfer_order sa

                  LEFT JOIN procurement_payment st ON sa.payment_order_id = st.id

         WHERE order_no = 'YKD202011090004'
     ) a

         NATURAL JOIN ( # 查询输入付款单供应商ID

    SELECT pt.payment_order_sn    '输入付款单',
           pt.supplier_account_id '输付供ID',
           pt.status              '付款单状态',
           pt.is_tax              '输入含税'
    FROM procurement_payment pt

    WHERE payment_order_sn = 'YFK202011090018') b;
