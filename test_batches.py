from datetime import date

from model import Batch, OrderLine

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

def test_allocating_to_a_batch_reduce_the_available_quantity():
    batch = Batch("batch-001", "SMALL_TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL_TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18

def test_can_allocate_if_avaialable_graeter_than_required():
    large_batch, smal_line = make_batch_and_line("ELEGANT_LAMP", 20, 2)
    assert large_batch.can_allocate(smal_line)

def test_cannot_allocate_if_avaialable_smaller_than_required():
    large_batch, smal_line = make_batch_and_line("ELEGANT_LAMP", 2, 20)
    assert large_batch.can_allocate(smal_line) is False

def test_can_allocate_if_avaialable_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT_LAMP", 2, 2)
    assert batch.can_allocate(line)

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCONFORTABLE_CHAIR", 100, eta=None)
    diferent_sku_line = OrderLine("order-123", "EXPENSIVE_TOASTER", 10)
    assert batch.can_allocate(diferent_sku_line) is False






