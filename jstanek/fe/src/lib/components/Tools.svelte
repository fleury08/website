<script lang="ts">

  import { defaultHashObject, defaultPasswordOptions, generatePassword, hashText } from "$lib/tools";
  import type { HashObject, PasswordOptions } from "$lib/types/tools";

  let passwordObject: PasswordOptions = defaultPasswordOptions()
  let hashObject: HashObject = defaultHashObject()
  let generated = {
    "password": "",
    "hash": ""
  }

  async function generatePasswordHandler() {
    generated.password = await generatePassword(passwordObject)
  }

  async function hashTextHandler() {
    generated.hash = await hashText(hashObject)
  }

</script>

<div id="tools-page"
     class="page">
  <div class="text-6xl text-center">Useful tools</div>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3 gap-4">
      <div class="col mb-4">
        <div class="card">
          <div class="card-header">
            Password Generator
          </div>
          <div class="card-body">
            <div class="w-100 mb-3">
              <label for="passwordLength">Password length</label>
              <input class="form-control"
                     type="number"
                     max="4096"
                     id="passwordLength"
                     bind:value={passwordObject.length}>
            </div>
            <div class="form-check mb-3">
              <input class="form-check-input"
                     type="checkbox"
                     bind:checked={passwordObject.uppercase}
                     id="passwordSubsetUppercase">
              <label class="form-check-label"
                     for="passwordSubsetUppercase">Uppercase letters [A-Z]</label>
            </div>
            <div class="form-check mb-3">
              <input class="form-check-input"
                     type="checkbox"
                     bind:checked={passwordObject.lowercase}
                     id="passwordSubsetLowercase">
              <label class="form-check-label"
                     for="passwordSubsetLowercase">Lowercase letters [a-z]</label>
            </div>
            <div class="form-check mb-3">
              <input class="form-check-input"
                     type="checkbox"
                     id="passwordSubsetNumbers"
                     bind:checked={passwordObject.numeric}>
              <label class="form-check-label"
                     for="passwordSubsetNumbers">Numbers [0-9]</label>
            </div>
            <div class="form-check mb-3">
              <input class="form-check-input"
                     type="checkbox"
                     bind:checked={passwordObject.special}
                     id="passwordSubsetSymbols">
              <label class="form-check-label"
                     for="passwordSubsetSymbols">Special characters [$#/...]</label>
            </div>
            <div class="w-100 mb-3">
              <label for="passwordOutput">Password</label>
              <textarea class="form-control"
                        rows="4"
                        id="passwordOutput">{generated.password}</textarea>
            </div>
            <div class="mb-3">
              <button class="btn btn-primary w-100"
                      id="passwordRegenerate"
                      on:click={generatePasswordHandler}
              >Generate
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="col mb-4">
        <div class="card">
          <div class="card-header">
            Hashing tool
          </div>
          <div class="card-body">
            <div class="w-100 mb-3">
              <label for="hashInput">Input to hash</label>
              <input type="text"
                     class="form-control"
                     id="hashInput"
                     bind:value={hashObject.text}
              >
            </div>
            <div class="w-100 mb-3">
              <label for="hashAlgSelect">Hashing algorithm</label>
              <select id="hashAlgSelect"
                      class="form-control"
                      bind:value={hashObject.alg}>
                <option value="sha-512">sha-512</option>
                <option value="sha-256">sha-256</option>
                <option value="sha1">sha1</option>
                <option value="md5">md5</option>
              </select>
            </div>
            <div class="w-100 mb-3">
								<textarea rows="5"
                          id="hashOutput"
                          class="form-control">{generated.hash}</textarea>
            </div>
            <div class="mb-3">
              <button class="btn btn-primary w-100"
                      id="hashGenerate"
                      on:click={hashTextHandler}
              >Generate
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="col mb-4 d-none">
        <div class="card">
          <div class="card-header">
            Base64
          </div>
          <div class="card-body">
            <div class="w-100 mb-3">
              <label for="base64EncodeInput"
                     class="form-label">Encode</label>
              <input id="base64EncodeInput"
                     class="form-control"
                     type="text" />
            </div>
            <div class="w-100 mb-3">
								<textarea id="base64EncodeOutput"
                          class="form-control"></textarea>
            </div>

            <div class="w-100 mb-3">
              <label for="base64DecodeInput"
                     class="form-label">Decode</label>
              <input id="base64DecodeInput"
                     class="form-control"
                     type="text" />
            </div>
            <div class="w-100 mb-3">
								<textarea class="form-control"
                          id="base64DecodeOutput"></textarea>
            </div>
          </div>
        </div>
      </div>

      <div class="col mb-4 d-none">
        <div class="card">
          <div class="card-header">
            MongoDB _id tool
          </div>
          <div class="card-body">
            <div class="w-100 mb-3">
              <label for="mongoDbIdInput"
                     class="form-label">_id</label>
              <input id="mongoDbIdInput"
                     class="form-control"
                     type="text" />
            </div>
            <div class="w-100 mb-3">
              <label for="mongoDbIdOutput"
                     class="form-label">Timestamp</label>
              <input type="text"
                     class="form-control"
                     id="mongoDbIdOutput">
            </div>
          </div>
        </div>
      </div>

      <div class="col mb-4">
        <div class="card">
          <div class="card-body">
            ... more to come. I'm working on it!
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
