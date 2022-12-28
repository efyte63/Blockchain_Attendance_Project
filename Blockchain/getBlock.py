def find_records(form, blockchain):
    for block in blockchain:
        print(block.data)
        condition = (block.data[0] == form.get("name") and
                    block.data[1] == form.get("date") and
                    block.data[2] == form.get("course") and
                    block.data[3] == form.get("year") and
                    block.data[4] == form.get("sem") and
                    len(block.data[5]) == int(form.get("number")))
        if condition:
            return block.data[5]
    return -1
