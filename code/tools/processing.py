import spacy


# ------------------------------------------------------
# Determine context depending on user input (sent, prev, next, both)
def determine_context(current_sentence, row, context):
    targetSentence = ""
    if context == "sent":
        targetSentence += row[current_sentence]
    if context == "prev":
        targetSentence += row["prevSentence"] + " [SEP] "
        targetSentence += row[current_sentence]
    if context == "next":
        targetSentence += row[current_sentence] + " [SEP] "
        targetSentence += row["nextSentence"]
    if context == "both":
        targetSentence += row["prevSentence"] + " [SEP] "
        targetSentence += row[current_sentence] + " [SEP] "
        targetSentence += row["nextSentence"]
    return targetSentence


# ------------------------------------------------------
# Given a predefined window around the masked expression
# of n tokens to the left and to the right, provide context
# for the masked expression. In this case, n is specified
# to be 3, as in Karsdorp et al.(2015).
def ngram_context(maskedS, targetE, window):
    window_context = []
    maskedS = maskedS.split()
    index_mask = maskedS.index("[MASK]")
    window_indices = []
    window_indices += range(index_mask - window, index_mask)
    window_indices.append(index_mask)
    window_indices += range(index_mask + 1, window + index_mask + 1)
    window_indices = [w for w in window_indices if w >= 0 and w < len(maskedS)]
    for i in range(len(maskedS)):
        if i in window_indices:
            window_context.append(maskedS[i])
    window_context = " ".join(window_context)
    unmasked_context = window_context.replace("[MASK]", targetE)
    return window_context, unmasked_context


# ------------------------------------------------------
# Remove the first token from the masked expression if
# it is a determiner or a number, and make it part of the
# context. For example, given the sentence "A little old
# man in a boat approached him and said":
# * Original masking:
#     -> [MASK] in a boat approached him and said
# * Replaced to:
#     -> A [MASK] in a boat approached him and said
def process_expression(target, masked_sentence, nlp):
    spacy_mask = nlp(target)
    first_token_mask = spacy_mask
    first_token_mask_pos = spacy_mask[0].pos_
    context_with_det = masked_sentence
    target_without_det = spacy_mask
    # If MASK has more than one token and first token is DET or NUM
    if first_token_mask_pos in ["DET", "NUM"] and len(spacy_mask) > 1: 
        # Remove DET or NUM from MASK, add it to context
        context_with_det = masked_sentence.replace('[MASK] ', '' + first_token_mask[0].text + ' [MASK] ')
        target_without_det = spacy_mask[1:]
        
    target_without_det = [t.text for t in target_without_det]
    target_without_det = " ".join(target_without_det)
        
    # Does the target expression consist only of a personal or possessive pronoun?
    is_prp = False
    if len(spacy_mask) == 1:
        if spacy_mask[0].tag_ in ["PRP", "PRP$"]:
            is_prp = True
            
    return context_with_det, target_without_det, is_prp

# ------------------------------------------------------
# Remove rows if the target expression is not unique and
# always belongs to the same label.
def drop_target_duplicates(tempdf):
    dExpAnimacy = dict()
    dCounts = dict()
    for i, row in tempdf.iterrows():
        if row['targetExpression'] in dExpAnimacy:
            dExpAnimacy[row['targetExpression']].add(row['animated'])
            dCounts[row['targetExpression']] += 1
        else:
            dExpAnimacy[row['targetExpression']] = {row['animated']}
            dCounts[row['targetExpression']] = 1

    dupl_to_remove = []
    for i in dExpAnimacy:
        if dCounts[i] > 1 and len(dExpAnimacy[i]) == 1:
            dupl_to_remove.append(i)
    storiesdf_uni = tempdf[~tempdf.targetExpression.isin(dupl_to_remove)]
    return storiesdf_uni