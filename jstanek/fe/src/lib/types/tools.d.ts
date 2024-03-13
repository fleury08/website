
export type PasswordOptions = {
  length: number
  numeric: boolean
  special: boolean
  uppercase: boolean
  lowercase: boolean
}


export type TextObject = {
  text: string
}

export type HashObject = TextObject & {
  alg: string
}


export type Base64Object = TextObject
export type MongoDbObject = {
  object_id: string
}

export default {}