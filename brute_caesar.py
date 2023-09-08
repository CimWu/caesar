def caesar(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted += decrypted_char
        else:
            decrypted += char
    return decrypted

ciphertext = "oggiawbuhvohqofrwoqoffsghvogbchcqqiffsrobrhvohhvsdsfgcbgvsorkogbchibrsfkohsfkvsbsldsfwsbqwbuhvsuogdfstzslhvsbslhghouscthvwgqczrgvcqyfsgdcbgswgvmdsfjsbhwzohwcbbcfaozzmhvwgghousctvmdsfjsbhwzohwcbgvcizrcbzmzoghogvcfhhwasoawbihscfgcpihhvsibsldsqhsrcbgshctvmdsfjsbhwzohwcbobrhvswbopwzwhmhcqcbhfczpfsohvwbuqobpfwbucbtsszwbugctdobwqkvwqvwbhifbqobdfczcbuhvsvmdsfjsbhwzohwcbdfczcbusrsdwgcrsgctvmdsfjsbhwzohwcbqobozgcfsgizhwbtowbhwbukvwqvkcizrcpjwcigzmzsorhcrfckbwbusjsbwttowbhwburcsgbhcqqifdscdzskvcdobwqofsacfszwyszmhcsldsfwsbqsgkwatowzifsobrrfckbwbu"

for shift in range(1, 26):
    decrypted = caesar(ciphertext, shift)
    print(f"Shift {shift}: {decrypted}")

ciphertext = "czggjviyrzgxjhzojjpmxmtkojbmvkctxgvnndkmjhdnzocvodordggwzdiozmznodibviytjprdgggzvmivojidatjpvmzrdggdibojkpodioczodhz"

for shift in range(1, 26):
    decrypted = caesar(ciphertext, shift)
    print(f"Shift {shift}: {decrypted}")

# Shift 14:
# assumingthatcardiacarresthasnotoccurredandthatthepersonsheadwasnotunderwaterwhenexperiencing
# thegaspreflexthenextstageofthiscoldshockresponseishyperventilationnormallythisstageof
# hyperventilationshouldonlylastashorttimeaminuteorsobuttheunexpectedonsetofhyperventilation
# andtheinabilitytocontrolbreathingcanbringonfeelingsofpanicwhichinturncanprolongthehyperventilation
# prolongedepisodesofhyperventilationcanalsoresultinfainting
# whichwouldobviouslyleadtodrowningeveniffaintingdoesntoccurpeoplewhopanicare
# morelikelytoexperienceswimfailureanddrowning


# Shift 21: helloandwelcometoourcryptographyclassipromise
# thatitwillbeinterestingandyouwilllearnatonifyouarewillingtoputinthetime
