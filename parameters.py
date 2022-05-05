class Parameters(object):
    seq_length = 30
    num_tags = 7

    keep_prob = 1
    lr = 0.0005

    num_epochs = 60        #epochs
    batch_size = 16          #batch_size


    train_filename='./data/experiment4/train1.txt'  #train data
    test_filename='./data/E2.txt'    #test data
    eva_filename = './data/experiment4/tst.txt'    #eva data
    vocab_filename='C:\Users\Administrator\PycharmProjects\pytest\ori-vocab.txt'        #vocabulary
    bert_config_file = './bert_model/English_L-4_H-512_A-8/bert_config.json'
    init_checkpoint = './bert_model/English_L-4_H-512_A-8/bert_model.ckpt'
